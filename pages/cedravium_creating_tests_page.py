from .base_page import BasePage
from .cedravium_page import LoginPage
from .locators import LoginPageLocators
from .locators import BasePageLocators
from .locators import CreateTestLocators


class CreateTestsPage(BasePage):
    def button_create_tests(self):
        assert self.is_element_present(*CreateTestLocators.BUTTON_CREATE_TEST)
        create_test = self.browser.find_element(*CreateTestLocators.BUTTON_CREATE_TEST)
        create_test.click()

    def filling_in_data_tests(self):
        title_test = self.browser.find_element(*CreateTestLocators.TITLE_TEST)
        title = self.random_text_generator(length=1000)
        title_test.send_keys(title)

    def adding_description(self, length):
        assert self.is_element_present(*CreateTestLocators.BUTTON_ADD_DESCRIPTION)
        click_add_description = self.browser.find_element(*CreateTestLocators.BUTTON_ADD_DESCRIPTION)
        click_add_description.click()
        assert self.is_element_present(*CreateTestLocators.INPUT_MY_DESCRIPTION)
        input_description = self.browser.find_element(*CreateTestLocators.INPUT_MY_DESCRIPTION)
        text = self.random_text_generator(length)
        input_description.send_keys(text)