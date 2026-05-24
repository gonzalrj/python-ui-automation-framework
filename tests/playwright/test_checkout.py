"""Checkout flow tests for Playwright."""

import pytest
import allure
from playwright.sync_api import Page

from pages.playwright.login_page import LoginPage
from pages.playwright.inventory_page import InventoryPage
from pages.playwright.cart_page import CartPage
from pages.playwright.checkout_step1_page import CheckoutStep1Page
from pages.playwright.checkout_step2_page import CheckoutStep2Page
from pages.playwright.checkout_complete_page import CheckoutCompletePage
from pages.playwright.components.header_component import HeaderComponent
from test_data import DataLoader


@allure.feature("Checkout")
class TestCheckoutPlaywright:

    @pytest.fixture
    def test_data_loader(self):
        """Provide test data loader."""
        return DataLoader()

    @allure.title("Checkout flow - add item to cart and complete purchase")
    @pytest.mark.playwright_checkout
    def test_checkout(self, page: Page, base_url, timeout, test_data_loader):
        ms = timeout * 1000

        with allure.step("Load test user and log in"):
            user = test_data_loader.get_user("valid_user")
            login_page = LoginPage(page, base_url=base_url, timeout=ms)
            login_page.navigate_to(base_url)
            login_page.login(user["username"], user["password"])

        with allure.step("Verify inventory is present and add first item to cart"):
            inventory_page = InventoryPage(page, timeout=ms)
            assert inventory_page.get_inventory_items_count() > 0, (
                "No inventory items found."
            )
            item_details = inventory_page.get_product_details_by_index(0)
            inventory_page.add_item_to_cart(0)

        with allure.step("Verify cart count and open cart"):
            header = HeaderComponent(page, timeout=ms)
            assert header.get_cart_item_count() == 1, (
                "Cart item count should be 1 after adding an item."
            )
            header.navigate_to_cart()

        with allure.step("Verify item in cart and proceed to checkout"):
            cart_page = CartPage(page, timeout=ms)
            item_details_in_cart = cart_page.get_product_details_by_index(0)
            assert item_details == item_details_in_cart, (
                "Item details in cart do not match the added item."
            )
            cart_page.checkout()

        with allure.step("Enter checkout information and continue"):
            checkout_step1 = CheckoutStep1Page(page, timeout=ms)
            checkout_step1.enter_checkout_information()
            checkout_step1.continue_checkout()

        with allure.step("Verify order summary details and finish checkout"):
            checkout_step2 = CheckoutStep2Page(page, timeout=ms)
            item_details_in_checkout = checkout_step2.get_product_details_by_index(0)
            assert item_details_in_cart == item_details_in_checkout, (
                "Item details in checkout do not match the cart item."
            )
            assert checkout_step2.is_payment_info_displayed(), (
                "Payment information is not displayed."
            )
            assert checkout_step2.is_shipping_info_displayed(), (
                "Shipping information is not displayed."
            )
            assert checkout_step2.is_price_total_info_displayed(), (
                "Price total information is not displayed."
            )
            checkout_step2.finish_checkout()

        with allure.step("Verify checkout completion"):
            checkout_complete = CheckoutCompletePage(page, timeout=ms)
            assert checkout_complete.is_complete_image_displayed(), (
                "Complete image is not displayed."
            )
            assert (
                checkout_complete.get_complete_header_text()
                == "Thank you for your order!"
            ), "Complete header text does not match expected."
            assert (
                checkout_complete.get_complete_message_text()
                == "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
            ), "Complete message text does not match expected."
