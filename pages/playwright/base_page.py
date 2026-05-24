"""Base page class for Playwright."""

from playwright.sync_api import Page, Locator


class BasePage:
    """Base class for all Playwright page objects."""

    def __init__(self, page: Page, base_url: str = None, timeout: int = 10000):
        self.page = page
        self.base_url = base_url
        self.timeout = timeout
        self.page.set_default_timeout(timeout)

    def navigate_to(self, url: str) -> None:
        """Navigate to a specific URL."""
        self.page.goto(url)

    def get_title(self) -> str:
        """Get the page title."""
        return self.page.title()

    def get_current_url(self) -> str:
        """Get the current URL."""
        return self.page.url

    def reload(self) -> None:
        """Reload the page."""
        self.page.reload()

    def clear_cache(self) -> None:
        """Clear browser context cache, cookies, and storage."""
        self.page.context.clear_cookies()
        self.page.evaluate(
            "window.localStorage.clear(); window.sessionStorage.clear();"
        )

    # --- Locator helpers ---

    def click(self, locator: Locator) -> None:
        """Click an element."""
        locator.click()

    def fill(self, locator: Locator, text: str) -> None:
        """Fill an input field."""
        locator.fill(text)

    def get_text(self, locator: Locator) -> str:
        """Get the text content of an element."""
        return locator.text_content()

    def is_visible(self, locator: Locator, timeout: int = None) -> bool:
        """Wait up to timeout for a locator to be visible; return False on timeout."""
        try:
            locator.wait_for(state="visible", timeout=timeout or self.timeout)
            return True
        except Exception:
            return False
