"""Base page class for Selenium."""

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    """Base class for all Selenium page objects."""

    def __init__(self, driver: WebDriver, base_url: str = None, timeout: int = 10):
        """
        Initialize the page object.

        Args:
            driver: Selenium WebDriver instance
            base_url: Base URL for the application
            timeout: Timeout for wait operations (seconds)
        """
        self.driver = driver
        self.base_url = base_url
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def navigate_to(self, url: str) -> None:
        """Navigate to a specific URL."""
        self.driver.get(url)

    def find_element(self, locator: tuple) -> WebElement:
        """Find an element using the locator tuple (By, value)."""
        return self.driver.find_element(*locator)

    def find_elements(self, locator: tuple) -> list:
        """Find multiple elements using the locator tuple."""
        return self.driver.find_elements(*locator)

    def wait_for_element(self, locator: tuple, timeout: int = None) -> WebElement:
        """Wait for an element to be present."""
        timeout = timeout or self.timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_element_visible(
        self, locator: tuple, timeout: int = None
    ) -> WebElement:
        """Wait for an element to be visible."""
        timeout = timeout or self.timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator: tuple) -> None:
        """Click an element."""
        element = self.wait_for_element_visible(locator)
        element.click()

    def type_text(self, locator: tuple, text: str) -> None:
        """Type text into an input field."""
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        """Get text from an element."""
        element = self.wait_for_element(locator)
        return element.text

    def is_element_visible(self, locator: tuple, timeout: int = 5) -> bool:
        """Check if an element is visible."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    def get_title(self) -> str:
        """Get the page title."""
        return self.driver.title

    def clear_cache(self) -> None:
        """Clear browser cache, cookies, and storage."""
        self.driver.delete_all_cookies()
        self.driver.execute_script(
            "window.localStorage.clear(); window.sessionStorage.clear();"
        )

    def get_current_url(self) -> str:
        """Get the current URL."""
        return self.driver.current_url
