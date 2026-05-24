"""Checkout Step 1 page object for Playwright."""

from playwright.sync_api import Locator

from .base_page import BasePage


class CheckoutStep1Page(BasePage):
    """Page object for the checkout information form."""

    _FIRST_NAME = "firstName"
    _LAST_NAME = "lastName"
    _POSTAL_CODE = "postalCode"
    _CONTINUE_BUTTON = "continue"

    @property
    def first_name_input(self) -> Locator:
        return self.page.get_by_test_id(self._FIRST_NAME)

    @property
    def last_name_input(self) -> Locator:
        return self.page.get_by_test_id(self._LAST_NAME)

    @property
    def postal_code_input(self) -> Locator:
        return self.page.get_by_test_id(self._POSTAL_CODE)

    @property
    def continue_button(self) -> Locator:
        return self.page.get_by_test_id(self._CONTINUE_BUTTON)

    def enter_checkout_information(self) -> None:
        """Fill in the checkout information form."""
        self.fill(self.first_name_input, "Johnny")
        self.fill(self.last_name_input, "QA Tester")
        self.fill(self.postal_code_input, "12345")

    def continue_checkout(self) -> None:
        """Click continue to proceed to order summary."""
        self.click(self.continue_button)
