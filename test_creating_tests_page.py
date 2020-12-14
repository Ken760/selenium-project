from pages.cedravium_page import LoginPage
from pages.cedravium_creating_tests_page import CreateTestsPage
import time


class TestCreateTests:
    # def test_creating_a_test_from_a_profile(self, browser):
    #     link = "http://cedravium.ru/#/"
    #     self.page = LoginPage(browser, link)
    #     self.create = CreateTestsPage(browser, link)
    #     self.page.open()
    #     self.page.go_to_profile_page()
    #     self.create.button_create_tests()

    def test_filling_in_the_test_with_random_data(self, browser):
        link = "http://cedravium.ru/#/"
        self.page = LoginPage(browser, link)
        self.create = CreateTestsPage(browser, link)
        self.page.open()
        self.page.go_to_profile_page()
        self.create.button_create_tests()
        # self.test_creating_a_test_from_a_profile(browser)
        self.create = CreateTestsPage(browser, '')
        self.create.filling_in_data_tests(length=10)
        self.create.adding_description(length=1000)
        self.create.adding_one_of_the_list_test()
        self.create.filling_questions(length=10)
        self.create.filling_answers_all_random(length=20)
        self.create.response_selecting()
        time.sleep(10)

