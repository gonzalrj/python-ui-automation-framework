"""Inventory page object for Playwright."""

from playwright.sync_api import Locator

from .base_page import BasePage


class InventoryPage(BasePage):
    """Page object for the inventory page."""

    _INVENTORY_ITEM = "inventory-item"
    _ITEM_NAME = "inventory-item-name"
    _ITEM_DESCRIPTION = "inventory-item-desc"
    _ITEM_PRICE = "inventory-item-price"
    _ADD_TO_CART_BUTTON = "Add to cart"

    @property
    def inventory_items(self) -> Locator:
        return self.page.get_by_test_id(self._INVENTORY_ITEM)

    def get_inventory_items_count(self) -> int:
        """Get the count of inventory items."""
        return self.inventory_items.count()

    def get_product_details_by_index(self, item_index: int) -> dict:
        """Get product details (name, description, price) by index."""
        item = self.inventory_items.nth(item_index)
        return {
            "name": item.get_by_test_id(self._ITEM_NAME).text_content(),
            "description": item.get_by_test_id(self._ITEM_DESCRIPTION).text_content(),
            "price": item.get_by_test_id(self._ITEM_PRICE).text_content(),
        }

    def add_item_to_cart(self, item_index: int) -> None:
        """Add an item to the cart by index."""
        self.inventory_items.nth(item_index).get_by_role(
            "button", name=self._ADD_TO_CART_BUTTON
        ).click()
