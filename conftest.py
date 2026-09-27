import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import generate_email, generate_password

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
def user():
    return {
        "name": "Vitaly",
        "email": generate_email(),        
        "password": generate_password()    
    }

@pytest.fixture
def short_password():
    return generate_password(length=5) 


def open_page(driver, path="/"):
    driver.get(BASE_URL + path)


def wait_and_click(wait, locator):
    wait.until(EC.element_to_be_clickable(locator)).click()


def wait_and_send_keys(wait, locator, text):
    wait.until(EC.visibility_of_element_located(locator)).send_keys(text)


def login(driver, wait, user):
    open_page(driver, "/login")
    from locators import Locators as L
    wait_and_send_keys(wait, L.LOGIN_EMAIL_INPUT, user["email"])
    wait_and_send_keys(wait, L.LOGIN_PASSWORD_INPUT, user["password"])
    wait_and_click(wait, L.LOGIN_SUBMIT)
    wait.until(EC.visibility_of_element_located(L.ORDER_BUTTON))
