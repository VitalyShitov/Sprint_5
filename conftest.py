import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "https://stellarburgers.education-services.ru"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)


@pytest.fixture
def valid_user_data():
    return {
        "name": "Vitaly",
        "email": "vitaly_shitov_54_999@example.com",
        "password": "TestPass123"
    }


@pytest.fixture
def short_password_data():
    return {
        "name": "Vitaly",
        "email": "vitaly_shitov_54_999@example.com",
        "password": "12345"
    }