"""Login page object for Playwright."""

from playwright.sync_api import Page, Locator

from .base_page import BasePage


class LoginPage(BasePage):
    """Page object for the login page."""

    _USERNAME = "username"
    _PASSWORD = "password"
    _LOGIN_BUTTON = "login-button"
    _ERROR = "error"

    @property
    def username_input(self) -> Locator:
        return self.page.get_by_test_id(self._USERNAME)

    @property
    def password_input(self) -> Locator:
        return self.page.get_by_test_id(self._PASSWORD)

    @property
    def login_button(self) -> Locator:
        return self.page.get_by_test_id(self._LOGIN_BUTTON)

    @property
    def error_message(self) -> Locator:
        return self.page.get_by_test_id(self._ERROR)

    def login(self, username: str, password: str) -> None:
        """Perform login with username and password."""
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.login_button)

    def get_error_message(self) -> str:
        """Get error message text if login fails."""
        return self.get_text(self.error_message)

    def is_error_displayed(self) -> bool:
        """Check if an error message is displayed."""
        return self.is_visible(self.error_message)
