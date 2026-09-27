from selenium.webdriver.support import expected_conditions as EC
from locators import Locators as L
from conftest import open_page, wait_and_send_keys, wait_and_click


class TestRegistration:

    def test_successful_registration(self, driver, wait, user):
        open_page(driver, "/register")
        wait_and_send_keys(wait, L.REG_NAME_INPUT, user["name"])
        wait_and_send_keys(wait, L.REG_EMAIL_INPUT, user["email"])
        wait_and_send_keys(wait, L.REG_PASSWORD_INPUT, user["password"])
        wait_and_click(wait, L.REG_SUBMIT)

        assert wait.until(EC.url_contains("/login"))

    def test_registration_fails_with_short_password(self, driver, wait, user, short_password):
        open_page(driver, "/register")
        wait_and_send_keys(wait, L.REG_NAME_INPUT, user["name"])
        wait_and_send_keys(wait, L.REG_EMAIL_INPUT, user["email"])
        wait_and_send_keys(wait, L.REG_PASSWORD_INPUT, short_password)  
        wait_and_click(wait, L.REG_SUBMIT)

        error = wait.until(EC.visibility_of_element_located(L.PASSWORD_ERROR))
        assert error.is_displayed()
        assert "Некорректный пароль" in error.text
