import os
import pytest
from selenium import webdriver
from constants import URL


@pytest.fixture
def driver():
    selenoid_url = os.getenv("SELENOID_URL")

    if selenoid_url:
        driver = webdriver.Remote(
            command_executor=selenoid_url,
            options=webdriver.ChromeOptions()
        )
    else:
        driver = webdriver.Chrome()

    driver.get(URL.BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()