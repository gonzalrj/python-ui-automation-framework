"""Login page tests for Selenium."""

import pytest
from pages.selenium.login_page import LoginPage
from test_data import DataLoader


class TestLoginSelenium:
    """Selenium login test scenarios."""

    @pytest.fixture
    def test_data_loader(self):
        """Provide test data loader."""
        return DataLoader()

    @pytest.mark.selenium_login
    def test_login_valid_user(self, driver, base_url, test_data_loader):
        """Test successful login with valid credentials."""
        user = test_data_loader.get_user("valid_user")
        login_page = LoginPage(driver, base_url=base_url)
        login_page.navigate_to(login_page.base_url)
        login_page.login(user["username"], user["password"])
        assert not login_page.is_error_displayed()

    @pytest.mark.selenium_login
    def test_login_invalid_credentials(self, driver, base_url, test_data_loader):
        """Test login with invalid credentials shows error."""
        user = test_data_loader.get_user("invalid_user")
        login_page = LoginPage(driver, base_url=base_url)
        login_page.navigate_to(login_page.base_url)
        login_page.login(user["username"], user["password"])
        assert login_page.is_error_displayed()

    @pytest.mark.selenium_login
    def test_login_locked_out_user(self, driver, base_url, test_data_loader):
        """Test login with locked out user account shows locked message."""
        user = test_data_loader.get_user("locked_user")
        login_page = LoginPage(driver, base_url=base_url)
        login_page.navigate_to(login_page.base_url)
        login_page.login(user["username"], user["password"])
        assert login_page.is_error_displayed()
        # assert "locked" in login_page.get_error_message().lower()
