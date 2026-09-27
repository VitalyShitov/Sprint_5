from selenium.webdriver.support import expected_conditions as EC
from locators import Locators as L
from conftest import open_page, wait_and_click, login


class TestPersonalCabinet:

    def test_navigate_to_personal_cabinet(self, driver, wait, user):
        login(driver, wait, user)
        wait_and_click(wait, L.HEADER_PERSONAL_CABINET)
        assert wait.until(EC.url_contains("/account/profile"))
        assert wait.until(EC.visibility_of_element_located(L.PROFILE_FORM)).is_displayed()

    def test_navigate_to_constructor_via_constructor_button(self, driver, wait, user):
        login(driver, wait, user)
        wait_and_click(wait, L.HEADER_PERSONAL_CABINET)
        wait_and_click(wait, L.HEADER_CONSTRUCTOR)
        assert wait.until(EC.url_matches(f"{open_page.__module__}"))  # главная
        assert wait.until(EC.visibility_of_element_located(
            ("xpath", '//h1[text()="Соберите бургер"]')
        ))

    def test_navigate_to_constructor_via_logo(self, driver, wait, user):
        login(driver, wait, user)
        wait_and_click(wait, L.HEADER_PERSONAL_CABINET)
        wait_and_click(wait, L.LOGO)
        assert wait.until(EC.url_matches("https://stellarburgers.education-services.ru/$"))

    def test_logout(self, driver, wait, user):
        login(driver, wait, user)
        wait_and_click(wait, L.HEADER_PERSONAL_CABINET)
        wait_and_click(wait, L.LOGOUT_BUTTON)
        assert wait.until(EC.url_contains("/login"))
