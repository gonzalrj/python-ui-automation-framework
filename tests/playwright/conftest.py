"""Playwright-specific pytest fixtures."""

import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page
from pages.playwright.login_page import LoginPage


@pytest.fixture
def playwright_browser(test_config):
    """Provide a Playwright browser instance."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=test_config["headless"])
        yield browser
        browser.close()


@pytest.fixture
def playwright_context(playwright_browser: Browser) -> BrowserContext:
    """Provide a Playwright browser context."""
    context = playwright_browser.new_context()
    yield context
    context.close()


@pytest.fixture
def playwright_page(playwright_context: BrowserContext) -> Page:
    """Provide a Playwright page instance."""
    page = playwright_context.new_page()
    yield page
    page.close()


@pytest.fixture
def login_page(playwright_page: Page, test_config):
    """Provide a LoginPage page object for Playwright."""
    return LoginPage(
        playwright_page,
        base_url=test_config["base_url"],
        timeout=test_config["timeout"] * 1000,
    )
