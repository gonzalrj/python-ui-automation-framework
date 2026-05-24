"""Inventory page object for Selenium."""

from selenium.webdriver.common.by import By
from .base_page import BasePage


class InventoryPage(BasePage):
    """Page object for the inventory page."""

    # Locators
    INVENTORY_ITEMS = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    INVENTORY_ADD_TO_CART_BTNS = (By.CSS_SELECTOR, "[data-test^='add-to-cart']")
    INVENTORY_ITEM_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    INVENTORY_ITEM_DESCRIPTIONS = (By.CSS_SELECTOR, "[data-test='inventory-item-desc']")
    INVENTORY_ITEM_PRICES = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")

    def get_inventory_items_count(self):
        """Get the count of inventory items."""
        items = self.find_elements(self.INVENTORY_ITEMS)
        return len(items)

    def get_product_details_by_index(self, item_index: int) -> dict:
        """Get product details (namem, description, price) by index."""
        items = self.find_elements(self.INVENTORY_ITEMS)
        if 0 <= item_index < len(items):
            name = items[item_index].find_element(*self.INVENTORY_ITEM_NAMES).text
            description = (
                items[item_index].find_element(*self.INVENTORY_ITEM_DESCRIPTIONS).text
            )
            price = items[item_index].find_element(*self.INVENTORY_ITEM_PRICES).text
            return {"name": name, "description": description, "price": price}
        return {}

    def add_item_to_cart(self, item_index: int) -> None:
        """Add an item to the cart by index."""
        items = self.find_elements(self.INVENTORY_ITEMS)
        if 0 <= item_index < len(items):
            add_button = items[item_index].find_element(
                *self.INVENTORY_ADD_TO_CART_BTNS
            )
            add_button.click()
