import pytest
import allure

from pages.selenium.cart_page import CartPage
from pages.selenium.checkout_complete_page import CheckoutCompletePage
from pages.selenium.checkout_step1_page import CheckoutStep1Page
from pages.selenium.checkout_step2_page import CheckoutStep2Page
from pages.selenium.components.header_component import HeaderComponent
from pages.selenium.inventory_page import InventoryPage
from pages.selenium.login_page import LoginPage
from test_data import DataLoader


@allure.feature("Checkout")
class TestCheckout:
    @pytest.fixture
    def test_data_loader(self):
        """Provide test data loader."""
        return DataLoader()

    @allure.title("Checkout flow - add item to cart and complete purchase")
    @pytest.mark.selenium_checkout
    def test_checkout(self, driver, base_url, test_data_loader):

        with allure.step("Load test user and log in"):
            user = test_data_loader.get_user("valid_user")
            login_page = LoginPage(driver)
            login_page.navigate_to(base_url)
            login_page.login(user["username"], user["password"])

        with allure.step("Verify inventory present and add first item to cart"):
            inventory_page = InventoryPage(driver)
            assert inventory_page.get_inventory_items_count() > 0, (
                "No inventory items found."
            )
            inventory_page.add_item_to_cart(0)
            item_details = inventory_page.get_product_details_by_index(0)

        with allure.step("Verify cart count and open cart"):
            page_header = HeaderComponent(driver)
            assert page_header.get_cart_item_count() == 1, (
                "Cart item count should be 1 after adding an item."
            )
            page_header.navigate_to_cart()

        with allure.step("Verify item in cart and proceed to checkout"):
            cart_page = CartPage(driver)
            item_details_in_cart = cart_page.get_product_details_by_index(0)
            assert item_details == item_details_in_cart, (
                "Item details in cart do not match the added item."
            )
            cart_page.checkout()

        with allure.step("Enter checkout information and continue"):
            checkout_step1_page = CheckoutStep1Page(driver)
            checkout_step1_page.enter_checkout_information()
            checkout_step1_page.continue_checkout()

        with allure.step("Verify checkout step 2 details and finish checkout"):
            checkout_step2_page = CheckoutStep2Page(driver)
            item_details_in_checkout = checkout_step2_page.get_product_details_by_index(
                0
            )
            assert item_details_in_cart == item_details_in_checkout, (
                "Item details in checkout do not match the cart item."
            )
            assert checkout_step2_page.is_payment_info_displayed(), (
                "Payment information is not displayed."
            )
            assert checkout_step2_page.is_shipping_info_displayed(), (
                "Shipping information is not displayed."
            )
            assert checkout_step2_page.is_price_total_info_displayed(), (
                "Price total information is not displayed."
            )
            checkout_step2_page.finish_checkout()

        with allure.step("Verify checkout completion"):
            checkout_complete_page = CheckoutCompletePage(driver)
            assert checkout_complete_page.is_complete_image_displayed(), (
                "Complete image is not displayed."
            )
            assert (
                checkout_complete_page.get_complete_header_text()
                == "Thank you for your order!"
            ), "Complete header text does not match expected."
            assert (
                checkout_complete_page.get_complete_message_text()
                == "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
            ), "Complete message text does not match expected."
