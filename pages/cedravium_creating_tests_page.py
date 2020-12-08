from .base_page import BasePage
from .cedravium_page import LoginPage
from .locators import LoginPageLocators
from .locators import BasePageLocators
from .locators import CreateTestLocators
import time


class CreateTestsPage(BasePage):
    def button_create_tests(self):
        # assert self.is_element_present(*CreateTestLocators.BUTTON_CREATE_TEST)
        create_test = self.browser.find_element(*CreateTestLocators.BUTTON_CREATE_TEST)
        create_test.click()
        time.sleep(10)