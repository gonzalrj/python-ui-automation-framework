"""Header component for Selenium."""

from selenium.webdriver.common.by import By
from pages.selenium.base_page import BasePage


class HeaderComponent(BasePage):
    """Header component for the inventory page."""

    # Locators
    SHOPPING_CART_LNK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    SHOPPING_CART_COUNT = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")

    def get_cart_item_count(self) -> int:
        """Get the number of items in the shopping cart."""
        if self.is_element_visible(self.SHOPPING_CART_COUNT):
            count_text = self.get_text(self.SHOPPING_CART_COUNT)
            return int(count_text)
        return 0

    def navigate_to_cart(self) -> None:
        """Navigate to the shopping cart page."""
        self.click(self.SHOPPING_CART_LNK)
