from .base_page import BasePage
# from .cedravium_page import LoginPage
# from .locators import LoginPageLocators
# from .locators import BasePageLocators
from .locators import CreateTestLocators
from time import sleep


class CreateTestsPage(BasePage):
    def button_create_tests(self):
        assert self.is_element_present(*CreateTestLocators.BUTTON_CREATE_TEST), "Button create test is not presented"
        create_test = self.browser.find_element(*CreateTestLocators.BUTTON_CREATE_TEST)
        create_test.click()

    def filling_in_data_tests(self, length):
        sleep(1)
        title_test = self.browser.find_element(*CreateTestLocators.TITLE_TEST)
        title = self.random_text_generator(length)
        title_test.send_keys(title)

    def adding_description(self, length):
        assert self.is_element_present(*CreateTestLocators.BUTTON_ADD_DESCRIPTION), \
            "Button add description is not presented"
        click_add_description = self.browser.find_element(*CreateTestLocators.BUTTON_ADD_DESCRIPTION)
        click_add_description.click()
        assert self.is_element_present(*CreateTestLocators.INPUT_MY_DESCRIPTION), \
            "Form description is not presented"
        input_description = self.browser.find_element(*CreateTestLocators.INPUT_MY_DESCRIPTION)
        text = self.random_text_generator(length)
        input_description.send_keys(text)
        sleep(1)

    def adding_one_of_the_list_test(self):
        assert self.is_element_present(*CreateTestLocators.BUTTON_ADD_TEST), "Button add test is not presented"
        button_add = self.browser.find_element(*CreateTestLocators.BUTTON_ADD_TEST)
        button_add.click()
        create_one_list = self.browser.find_element(*CreateTestLocators.TEST_ONE_OF_THE_LIST)
        create_one_list.click()
        assert self.is_element_present(*CreateTestLocators.TEST_FORM), "The test form did not appear"

    def filling_out_the_one_of_the_list_form(self):
        pass

    def filling_questions(self, length):
        question = self.browser.find_element(*CreateTestLocators.QUESTION_NAME)
        text_question = self.random_text_generator(length)
        question.send_keys(text_question)

    def filling_answers(self, first, second):
        first_answers = self.browser.find_element(*CreateTestLocators.ANSWERS_FIELD1)
        text1 = self.random_text_generator(first)
        text2 = self.random_text_generator(second)
        first_answers.send_keys(text1)
        second_answers = self.browser.find_element(*CreateTestLocators.ANSWERS_FIELD2)
        second_answers.send_keys(text2)