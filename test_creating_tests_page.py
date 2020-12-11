from pages.cedravium_page import LoginPage
from pages.cedravium_creating_tests_page import CreateTestsPage
from pages.base_page import BasePage
import pytest
import time


class TestCreateTests:
    def test_creating_a_test_from_a_profile(self, browser):
        link = "http://cedravium.ru/#/"
        self.page = LoginPage(browser, link)
        self.create = CreateTestsPage(browser, link)
        self.page.open()
        self.page.go_to_profile_page()
        self.create.button_create_tests()
        self.create.filling_in_data_tests()
        self.create.adding_description(length=1000)


