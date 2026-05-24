"""Checkout Step 1 page object for Selenium."""

from selenium.webdriver.common.by import By
from .base_page import BasePage


class CheckoutStep1Page(BasePage):
    """Page object for the checkout step 1 page."""

    # Locators
    INPUT_FIRST_NAME = (By.CSS_SELECTOR, "[data-test='firstName']")
    INPUT_LAST_NAME = (By.CSS_SELECTOR, "[data-test='lastName']")
    INPUT_POSTAL_CODE = (By.CSS_SELECTOR, "[data-test='postalCode']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-test='continue']")

    def enter_checkout_information(self) -> None:
        """Enter checkout information and continue."""
        self.type_text(self.INPUT_FIRST_NAME, "Johnny")
        self.type_text(self.INPUT_LAST_NAME, "QA Tester")
        self.type_text(self.INPUT_POSTAL_CODE, "12345")

    def continue_checkout(self) -> None:
        """Continue to the next step of checkout."""
        self.click(self.CONTINUE_BUTTON)
