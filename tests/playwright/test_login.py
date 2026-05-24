"""Login page tests for Playwright."""

import pytest
import allure
from playwright.sync_api import Page

from pages.playwright.login_page import LoginPage
from test_data import DataLoader


@allure.feature("Login")
class TestLoginPlaywright:

    @pytest.fixture
    def test_data_loader(self):
        return DataLoader()

    @allure.title("Login - valid credentials succeed")
    @pytest.mark.playwright_login
    def test_login_valid_user(self, page: Page, base_url, timeout, test_data_loader):
        with allure.step("Load valid user and navigate to login page"):
            user = test_data_loader.get_user("valid_user")
            login_page = LoginPage(page, base_url=base_url, timeout=timeout * 1000)
            login_page.navigate_to(base_url)

        with allure.step("Submit valid credentials"):
            login_page.login(user["username"], user["password"])

        with allure.step("Verify no error is displayed"):
            assert not login_page.is_error_displayed()

    @allure.title("Login - invalid credentials show error")
    @pytest.mark.playwright_login
    def test_login_invalid_credentials(self, page: Page, base_url, timeout, test_data_loader):
        with allure.step("Load invalid user and navigate to login page"):
            user = test_data_loader.get_user("invalid_user")
            login_page = LoginPage(page, base_url=base_url, timeout=timeout * 1000)
            login_page.navigate_to(base_url)

        with allure.step("Submit invalid credentials"):
            login_page.login(user["username"], user["password"])

        with allure.step("Verify error is displayed"):
            assert login_page.is_error_displayed()

    @allure.title("Login - locked out user shows error")
    @pytest.mark.playwright_login
    def test_login_locked_out_user(self, page: Page, base_url, timeout, test_data_loader):
        with allure.step("Load locked user and navigate to login page"):
            user = test_data_loader.get_user("locked_user")
            login_page = LoginPage(page, base_url=base_url, timeout=timeout * 1000)
            login_page.navigate_to(base_url)

        with allure.step("Submit locked user credentials"):
            login_page.login(user["username"], user["password"])

        with allure.step("Verify error is displayed"):
            assert login_page.is_error_displayed()
