"""Shared pytest fixtures and configuration."""

import pytest


def pytest_addoption(parser):
    """Register custom command line options."""
    parser.addoption(
        "--base-url",
        action="store",
        default="https://www.saucedemo.com/",
        help="Base URL for UI tests",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=True,
        help="Run browsers in headless mode",
    )


@pytest.fixture
def base_url(request):
    """Provide the base URL for tests."""
    return request.config.getoption("--base-url")


@pytest.fixture
def timeout():
    """Provide the default wait timeout for tests."""
    return 10


@pytest.fixture
def headless(request):
    """Provide the headless mode flag for tests."""
    return request.config.getoption("--headless")


@pytest.fixture
def test_config(base_url, timeout, headless):
    """Provide test configuration."""
    return {
        "base_url": base_url,
        "timeout": timeout,
        "headless": headless,
    }
