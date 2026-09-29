
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators as L
from helpers import open_page, wait_and_send_keys, wait_and_click


class TestRegistration:

    def test_successful_registration(self, driver, wait, valid_user_data):
        open_page(driver, "/register")
        wait_and_send_keys(wait, L.REG_NAME_INPUT, valid_user_data["name"])
        wait_and_send_keys(wait, L.REG_EMAIL_INPUT, valid_user_data["email"])
        wait_and_send_keys(wait, L.REG_PASSWORD_INPUT, valid_user_data["password"])
        wait_and_click(wait, L.REG_SUBMIT)

        assert wait.until(EC.url_contains("/login"))

    def test_registration_fails_with_short_password(self, driver, wait, short_password_data):
        open_page(driver, "/register")
        wait_and_send_keys(wait, L.REG_NAME_INPUT, short_password_data["name"])
        wait_and_send_keys(wait, L.REG_EMAIL_INPUT, short_password_data["email"])
        wait_and_send_keys(wait, L.REG_PASSWORD_INPUT, short_password_data["password"])
        wait_and_click(wait, L.REG_SUBMIT)

        error = wait.until(EC.visibility_of_element_located(L.PASSWORD_ERROR))
        assert error.is_displayed()
        assert "Некорректный пароль" in error.text