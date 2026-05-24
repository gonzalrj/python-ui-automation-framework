"""Shared pytest fixtures and configuration."""

import pytest


def pytest_addoption(parser):
    """Register custom command line options."""
    try:
        parser.addoption(
            "--base-url",
            action="store",
            default="https://www.saucedemo.com/",
            help="Base URL for UI tests",
        )
    except ValueError:
        pass  # pytest-playwright already registered this option

    parser.addoption(
        "--headless",
        action="store_true",
        default=True,
        help="Run browsers in headless mode",
    )


@pytest.fixture(scope="session")
def base_url(pytestconfig):
    """Provide the base URL for tests."""
    return pytestconfig.getoption("base_url") or "https://www.saucedemo.com/"


@pytest.fixture(scope="session")
def timeout():
    """Provide the default wait timeout in seconds."""
    return 10


@pytest.fixture(scope="session")
def headless(pytestconfig):
    """Provide the headless mode flag for tests."""
    return pytestconfig.getoption("--headless")


@pytest.fixture(scope="session")
def test_config(base_url, timeout, headless):
    """Provide test configuration."""
    return {
        "base_url": base_url,
        "timeout": timeout,
        "headless": headless,
    }
