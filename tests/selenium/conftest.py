import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():

    options = webdriver.ChromeOptions()

    options.binary_location = "/usr/bin/chromium"

    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    service = Service("/usr/bin/chromedriver")

    selenium_driver = webdriver.Chrome(service=service, options=options)

    yield selenium_driver

    selenium_driver.quit()
