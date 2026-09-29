from selenium.webdriver.support import expected_conditions as EC
from locators import Locators as L
from helpers import open_page, wait_and_click, login


class TestPersonalCabinet:

    def test_navigate_to_personal_cabinet(self, driver, wait, valid_user_data):
        login(driver, wait, valid_user_data)
        wait_and_click(wait, L.HEADER_PERSONAL_CABINET)

        assert wait.until(EC.url_contains("/account/profile"))
        assert wait.until(EC.visibility_of_element_located(L.PROFILE_FORM)).is_displayed()

    def test_navigate_to_constructor_via_constructor_button(self, driver, wait, valid_user_data):
        login(driver, wait, valid_user_data)
        wait_and_click(wait, L.HEADER_PERSONAL_CABINET)
        wait_and_click(wait, L.HEADER_CONSTRUCTOR)

        assert wait.until(EC.url_contains("/")) 
        assert wait.until(
            EC.visibility_of_element_located(("xpath", '//h1[text()="Соберите бургер"]'))
        ).is_displayed()

    def test_navigate_to_constructor_via_logo(self, driver, wait, valid_user_data):
        login(driver, wait, valid_user_data)
        wait_and_click(wait, L.HEADER_PERSONAL_CABINET)
        wait_and_click(wait, L.LOGO)

        assert wait.until(EC.url_contains("/"))

    def test_logout(self, driver, wait, valid_user_data):
        login(driver, wait, valid_user_data)
        wait_and_click(wait, L.HEADER_PERSONAL_CABINET)
        wait_and_click(wait, L.LOGOUT_BUTTON)

        assert wait.until(EC.url_contains("/login"))
