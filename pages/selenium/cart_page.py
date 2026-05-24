"""Cart page object for Selenium."""

from selenium.webdriver.common.by import By
from .base_page import BasePage


class CartPage(BasePage):
    """Page object for the cart page."""

    # Locators
    CART_ITEMS = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    CART_ITEM_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    CART_ITEM_DESCRIPTIONS = (By.CSS_SELECTOR, "[data-test='inventory-item-desc']")
    CART_ITEM_PRICES = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")

    def get_product_details_by_index(self, item_index: int) -> dict:
        """Get product details (namem, description, price) by index."""
        items = self.find_elements(self.CART_ITEMS)
        if 0 <= item_index < len(items):
            name = items[item_index].find_element(*self.CART_ITEM_NAMES).text
            description = (
                items[item_index].find_element(*self.CART_ITEM_DESCRIPTIONS).text
            )
            price = items[item_index].find_element(*self.CART_ITEM_PRICES).text
            return {"name": name, "description": description, "price": price}
        return {}

    def checkout(self) -> None:
        """Click the checkout button."""
        checkout_button = self.find_element((By.CSS_SELECTOR, "[data-test='checkout']"))
        checkout_button.click()
