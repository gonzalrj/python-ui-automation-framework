"""Login page object for Playwright."""

from .base_page import BasePage


class LoginPage(BasePage):
    """Page object for the login page."""

    # Selectors
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = ".error-message"

    def login(self, username: str, password: str) -> None:
        """Perform login with username and password."""
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        """Get error message if login fails."""
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_displayed(self) -> bool:
        """Check if error message is displayed."""
        return self.is_element_visible(self.ERROR_MESSAGE)
