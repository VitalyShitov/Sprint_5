from selenium.webdriver.support import expected_conditions as EC
from locators import Locators as L
from conftest import open_page, wait_and_click


class TestConstructor:

    def test_constructor_buns_section(self, driver, wait):
        open_page(driver)
        wait_and_click(wait, L.TAB_SAUCES)
        wait_and_click(wait, L.TAB_BUNS)
        assert wait.until(EC.visibility_of_element_located(L.TAB_BUNS_CURRENT)).is_displayed()

    def test_constructor_sauces_section(self, driver, wait):
        open_page(driver)
        wait_and_click(wait, L.TAB_SAUCES)
        assert wait.until(EC.visibility_of_element_located(L.TAB_SAUCES_CURRENT)).is_displayed()

    def test_constructor_fillings_section(self, driver, wait):
        open_page(driver)
        wait_and_click(wait, L.TAB_FILLINGS)
        assert wait.until(EC.visibility_of_element_located(L.TAB_FILLINGS_CURRENT)).is_displayed()
