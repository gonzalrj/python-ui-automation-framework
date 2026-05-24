"""Checkout Complete page object for Selenium."""

from selenium.webdriver.common.by import By
from .base_page import BasePage


class CheckoutCompletePage(BasePage):
    """Page object for the checkout complete page."""

    # Locators
    COMPLETE_IMAGE = (By.CSS_SELECTOR, "[data-test='pony-express']")
    COMPLETE_HEADER = (By.CSS_SELECTOR, "[data-test='complete-header']")
    COMPLETE_MESSAGE = (By.CSS_SELECTOR, "[data-test='complete-text']")

    def is_complete_image_displayed(self) -> bool:
        """Check if the complete image is displayed."""
        return self.is_element_visible(self.COMPLETE_IMAGE)

    def get_complete_header_text(self) -> str:
        """Get the text of the complete header."""
        return self.get_text(self.COMPLETE_HEADER)

    def get_complete_message_text(self) -> str:
        """Get the text of the complete message."""
        return self.get_text(self.COMPLETE_MESSAGE)
