from selenium.webdriver.support import expected_conditions as EC
from locators import Locators as L
from helpers import open_page, wait_and_click


class TestLogin:
    def test_login_from_main_via_login_button(self, driver, wait):
        open_page(driver, "/")
        wait_and_click(wait, L.LOGIN_BUTTON_MAIN)
        assert wait.until(EC.url_contains("/login"))

    def test_login_via_personal_cabinet_button(self, driver, wait):
        open_page(driver, "/")
        wait_and_click(wait, L.HEADER_PERSONAL_CABINET)
        assert wait.until(EC.url_contains("/login"))

    def test_login_via_register_form_button(self, driver, wait):
        open_page(driver, "/register")
        wait_and_click(wait, L.REG_LOGIN_LINK)
        assert wait.until(EC.url_contains("/login"))

    def test_login_via_restore_password_form_button(self, driver, wait):
        open_page(driver, "/forgot-password")
        wait_and_click(wait, L.RESTORE_LOGIN_LINK)
        assert wait.until(EC.url_contains("/login"))

