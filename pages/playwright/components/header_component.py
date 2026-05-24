"""Header component for Playwright."""

from playwright.sync_api import Locator

from pages.playwright.base_page import BasePage


class HeaderComponent(BasePage):
    """Shared page header with cart navigation."""

    _CART_LINK = "shopping-cart-link"
    _CART_BADGE = "shopping-cart-badge"

    @property
    def cart_link(self) -> Locator:
        return self.page.get_by_test_id(self._CART_LINK)

    @property
    def cart_badge(self) -> Locator:
        return self.page.get_by_test_id(self._CART_BADGE)

    def get_cart_item_count(self) -> int:
        """Get the number of items shown in the cart badge."""
        if self.cart_badge.is_visible():
            return int(self.cart_badge.text_content())
        return 0

    def navigate_to_cart(self) -> None:
        """Click the cart icon to open the cart page."""
        self.click(self.cart_link)
