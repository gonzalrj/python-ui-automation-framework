"""Playwright-specific pytest fixtures."""

import pytest


@pytest.fixture(scope="session", autouse=True)
def set_test_id_attribute(playwright):
    """Use data-test as the test ID attribute instead of the default data-testid."""
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args, headless):
    """Control headless mode via the shared --headless flag."""
    return {**browser_type_launch_args, "headless": headless}
