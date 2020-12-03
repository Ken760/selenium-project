from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
import random
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.SIGN_UP), "sign up is not presented"
        login_link = self.browser.find_element(*LoginPageLocators.SIGN_UP)
        login_link.click()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def random_password_generator(self, length=10):
        password = list('abcdefghijklmnopqrstuvwxyz1234567890')
        random.shuffle(password)
        password = ''.join([random.choice(password) for x in range(length)])
        return password

    def register_new_user(self, login, email, password):
        login_field = self.browser.find_element(*LoginPageLocators.LOGIN_INPUT_SIGN_UP)
        login_field.send_keys(login)
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT_SIGN_UP)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_SIGN_UP)
        password_field.send_keys(password)
        confirm_password_field = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_INPUT_SIGN_UP)
        confirm_password_field.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        button_register.click()
        time.sleep(1)

    def go_to_home_page(self):
        assert self.is_element_present(*BasePageLocators.HOME_PAGE), \
            "Button form is not presented"
        button_go_to_home_page = self.browser.find_element(*BasePageLocators.HOME_PAGE)
        button_go_to_home_page.click()

    def should_be_my_profile(self):
        assert self.is_element_present(*BasePageLocators.MY_PROFILE), \
            "My Profile is not presented"







