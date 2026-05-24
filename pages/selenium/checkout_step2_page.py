"""Checkout Step 2 page object for Selenium."""

from selenium.webdriver.common.by import By
from .base_page import BasePage


class CheckoutStep2Page(BasePage):
    """Page object for the checkout step 2 page."""

    # Locators
    CART_ITEMS = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    CART_ITEM_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    CART_ITEM_DESCRIPTIONS = (By.CSS_SELECTOR, "[data-test='inventory-item-desc']")
    CART_ITEM_PRICES = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    PAYMENT_INFO_VALUE = (By.CSS_SELECTOR, "[data-test='payment-info-value']")
    SHIPPING_INFO_VALUE = (By.CSS_SELECTOR, "[data-test='shipping-info-value']")
    ITEM_TOTAL_VALUE = (By.CSS_SELECTOR, "[data-test='subtotal-label']")
    TAX_VALUE = (By.CSS_SELECTOR, "[data-test='tax-label']")
    TOTAL_VALUE = (By.CSS_SELECTOR, "[data-test='total-label']")
    FINISH_BUTTON = (By.CSS_SELECTOR, "[data-test='finish']")

    def get_product_details_by_index(self, item_index: int) -> dict:
        """Get product details (namem, description, price) by index."""
        items = self.find_elements((By.CSS_SELECTOR, "[data-test='inventory-item']"))
        if 0 <= item_index < len(items):
            name = items[item_index].find_element(*self.CART_ITEM_NAMES).text
            description = (
                items[item_index].find_element(*self.CART_ITEM_DESCRIPTIONS).text
            )
            price = items[item_index].find_element(*self.CART_ITEM_PRICES).text
            return {"name": name, "description": description, "price": price}
        return {}

    def is_payment_info_displayed(self) -> bool:
        """Check if payment information is displayed."""
        return self.is_element_visible(self.PAYMENT_INFO_VALUE)

    def is_shipping_info_displayed(self) -> bool:
        """Check if shipping information is displayed."""
        return self.is_element_visible(self.SHIPPING_INFO_VALUE)

    def is_price_total_info_displayed(self) -> bool:
        """Check if item total, tax, and total information are displayed."""
        return (
            self.is_element_visible(self.ITEM_TOTAL_VALUE)
            and self.is_element_visible(self.TAX_VALUE)
            and self.is_element_visible(self.TOTAL_VALUE)
        )

    def finish_checkout(self) -> None:
        """Click the finish button to complete the checkout."""
        self.click(self.FINISH_BUTTON)
