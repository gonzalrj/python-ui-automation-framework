"""Base page class for Playwright."""

from playwright.sync_api import Page, expect


class BasePage:
    """Base class for all Playwright page objects."""

    def __init__(self, page: Page, base_url: str = None, timeout: int = 10000):
        """
        Initialize the page object.

        Args:
            page: Playwright Page instance
            base_url: Base URL for the application
            timeout: Timeout for wait operations (milliseconds)
        """
        self.page = page
        self.base_url = base_url
        self.timeout = timeout
        self.page.set_default_timeout(timeout)

    def navigate_to(self, url: str) -> None:
        """Navigate to a specific URL."""
        self.page.goto(url)

    def click(self, selector: str) -> None:
        """Click an element."""
        self.page.click(selector)

    def type_text(self, selector: str, text: str) -> None:
        """Type text into an input field."""
        self.page.fill(selector, text)

    def get_text(self, selector: str) -> str:
        """Get text from an element."""
        return self.page.text_content(selector)

    def is_element_visible(self, selector: str, timeout: int = None) -> bool:
        """Check if an element is visible."""
        timeout = timeout or self.timeout
        try:
            self.page.locator(selector).is_visible(timeout=timeout)
            return True
        except Exception:
            return False

    def wait_for_element(self, selector: str, timeout: int = None) -> None:
        """Wait for an element to be present."""
        timeout = timeout or self.timeout
        self.page.locator(selector).wait_for(timeout=timeout)

    def get_title(self) -> str:
        """Get the page title."""
        return self.page.title()

    def clear_cache(self) -> None:
        """Clear browser context cache, cookies, and storage."""
        self.page.context.clear_cookies()
        self.page.evaluate(
            "window.localStorage.clear(); window.sessionStorage.clear();"
        )

    def get_current_url(self) -> str:
        """Get the current URL."""
        return self.page.url

    def reload(self) -> None:
        """Reload the page."""
        self.page.reload()
