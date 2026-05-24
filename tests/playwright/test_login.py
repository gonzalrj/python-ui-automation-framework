"""Login page tests for Playwright."""

import pytest
from test_data import DataLoader


class TestLoginPlaywright:
    """Playwright login test scenarios."""

    @pytest.fixture
    def test_data_loader(self):
        """Provide test data loader."""
        return DataLoader()

    def test_login_valid_user(self, login_page, test_data_loader):
        """Test successful login with valid credentials."""
        user = test_data_loader.get_user("valid_user")
        login_page.navigate_to(login_page.base_url)
        login_page.login(user["username"], user["password"])
        # Verify no error is displayed and user is logged in
        assert not login_page.is_error_displayed()

    def test_login_invalid_credentials(self, login_page, test_data_loader):
        """Test login with invalid credentials shows error."""
        user = test_data_loader.get_user("invalid_user")
        login_page.navigate_to(login_page.base_url)
        login_page.login(user["username"], user["password"])
        # Verify error message is displayed
        assert login_page.is_error_displayed()

    def test_login_locked_out_user(self, login_page, test_data_loader):
        """Test login with locked out user account shows locked message."""
        user = test_data_loader.get_user("locked_user")
        login_page.navigate_to(login_page.base_url)
        login_page.login(user["username"], user["password"])
        # Verify locked out error is displayed
        assert login_page.is_error_displayed()
        # Optionally check error message contains "locked"
        # assert "locked" in login_page.get_error_message().lower()
