from pages.cedravium_page import LoginPage
from pages.base_page import BasePage
import time
import faker
import pytest


# def test_login(browser):
#     link = 'http://cedravium.ru/#/'
#     login = LoginPage(browser, link)
#     login.open()
#     login.go_to_sign_up_page()
#     login.should_be_login_form()
#     login.should_be_register_form()

# class TestRegistration():
#     def test_registration_new_user(self, browser):
#         link = "http://cedravium.ru/#/auth"
#         self.login_page = LoginPage(browser, link)
#         self.base_page = BasePage(browser, link)
#         self.login_page.open()
#         self.login_page.should_be_register_form()
#         fake = faker.Faker()
#         email = fake.email()
#         login = "test"
#         password = self.login_page.random_password_generator()
#         self.login_page.register_new_user(login, email, password)
#         self.login_page.go_to_home_page()
#         self.base_page.should_be_authorized_user()

class TestAuthorization():
    def test_sign_in_user(self, browser):
        link = "http://cedravium.ru/#/"
        self.login_page = LoginPage(browser, link)
        self.login_page.open()
        self.login_page.should_be_login_page()
        self.login_page.go_to_home_page()

    def test_incorrect_sign_in_user(self, browser):
        link = "http://cedravium.ru/#/"
        self.login_page = LoginPage(browser, link)
        self.login_page.open()
        self.login_page.should_be_login_url()
        fake = faker.Faker()
        email = fake.email()
        password = fake.password()
        self.login_page.user_authorization(email, password)
        self.login_page.go_to_home_page()












