"""Checkout Step 2 (order summary) page object for Playwright."""

from playwright.sync_api import Locator

from .base_page import BasePage


class CheckoutStep2Page(BasePage):
    """Page object for the order summary page."""

    _CART_ITEM = "inventory-item"
    _ITEM_NAME = "inventory-item-name"
    _ITEM_DESCRIPTION = "inventory-item-desc"
    _ITEM_PRICE = "inventory-item-price"
    _PAYMENT_INFO_VALUE = "payment-info-value"
    _SHIPPING_INFO_VALUE = "shipping-info-value"
    _SUBTOTAL_LABEL = "subtotal-label"
    _TAX_LABEL = "tax-label"
    _TOTAL_LABEL = "total-label"
    _FINISH_BUTTON = "finish"

    @property
    def cart_items(self) -> Locator:
        return self.page.get_by_test_id(self._CART_ITEM)

    @property
    def payment_info_value(self) -> Locator:
        return self.page.get_by_test_id(self._PAYMENT_INFO_VALUE)

    @property
    def shipping_info_value(self) -> Locator:
        return self.page.get_by_test_id(self._SHIPPING_INFO_VALUE)

    @property
    def subtotal_label(self) -> Locator:
        return self.page.get_by_test_id(self._SUBTOTAL_LABEL)

    @property
    def tax_label(self) -> Locator:
        return self.page.get_by_test_id(self._TAX_LABEL)

    @property
    def total_label(self) -> Locator:
        return self.page.get_by_test_id(self._TOTAL_LABEL)

    @property
    def finish_button(self) -> Locator:
        return self.page.get_by_test_id(self._FINISH_BUTTON)

    def get_product_details_by_index(self, item_index: int) -> dict:
        """Get product details (name, description, price) by index."""
        item = self.cart_items.nth(item_index)
        return {
            "name": item.get_by_test_id(self._ITEM_NAME).text_content(),
            "description": item.get_by_test_id(self._ITEM_DESCRIPTION).text_content(),
            "price": item.get_by_test_id(self._ITEM_PRICE).text_content(),
        }

    def is_payment_info_displayed(self) -> bool:
        """Check if payment information is displayed."""
        return self.is_visible(self.payment_info_value)

    def is_shipping_info_displayed(self) -> bool:
        """Check if shipping information is displayed."""
        return self.is_visible(self.shipping_info_value)

    def is_price_total_info_displayed(self) -> bool:
        """Check if subtotal, tax, and total labels are all displayed."""
        return (
            self.is_visible(self.subtotal_label)
            and self.is_visible(self.tax_label)
            and self.is_visible(self.total_label)
        )

    def finish_checkout(self) -> None:
        """Click finish to complete the order."""
        self.click(self.finish_button)
