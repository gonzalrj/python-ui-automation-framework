"""Checkout Complete page object for Playwright."""

from playwright.sync_api import Locator

from .base_page import BasePage


class CheckoutCompletePage(BasePage):
    """Page object for the order confirmation page."""

    _COMPLETE_IMAGE = "pony-express"
    _COMPLETE_HEADER = "complete-header"
    _COMPLETE_MESSAGE = "complete-text"

    @property
    def complete_image(self) -> Locator:
        return self.page.get_by_test_id(self._COMPLETE_IMAGE)

    @property
    def complete_header(self) -> Locator:
        return self.page.get_by_test_id(self._COMPLETE_HEADER)

    @property
    def complete_message(self) -> Locator:
        return self.page.get_by_test_id(self._COMPLETE_MESSAGE)

    def is_complete_image_displayed(self) -> bool:
        """Check if the confirmation image is displayed."""
        return self.is_visible(self.complete_image)

    def get_complete_header_text(self) -> str:
        """Get the confirmation header text."""
        return self.get_text(self.complete_header)

    def get_complete_message_text(self) -> str:
        """Get the confirmation message text."""
        return self.get_text(self.complete_message)
