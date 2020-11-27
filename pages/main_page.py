from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasePageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.SIGN_UP)
        link.click()


