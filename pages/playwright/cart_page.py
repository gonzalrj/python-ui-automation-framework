"""Cart page object for Playwright."""

from playwright.sync_api import Locator

from .base_page import BasePage


class CartPage(BasePage):
    """Page object for the cart page."""

    _CART_ITEM = "inventory-item"
    _ITEM_NAME = "inventory-item-name"
    _ITEM_DESCRIPTION = "inventory-item-desc"
    _ITEM_PRICE = "inventory-item-price"
    _CHECKOUT_BUTTON = "checkout"

    @property
    def cart_items(self) -> Locator:
        return self.page.get_by_test_id(self._CART_ITEM)

    @property
    def checkout_button(self) -> Locator:
        return self.page.get_by_test_id(self._CHECKOUT_BUTTON)

    def get_product_details_by_index(self, item_index: int) -> dict:
        """Get product details (name, description, price) by index."""
        item = self.cart_items.nth(item_index)
        return {
            "name": item.get_by_test_id(self._ITEM_NAME).text_content(),
            "description": item.get_by_test_id(self._ITEM_DESCRIPTION).text_content(),
            "price": item.get_by_test_id(self._ITEM_PRICE).text_content(),
        }

    def checkout(self) -> None:
        """Click the checkout button."""
        self.click(self.checkout_button)
