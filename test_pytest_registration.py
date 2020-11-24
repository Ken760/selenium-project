#pytest -s -v --browser_name=chrome test_pytest_registration.py
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.common.keys import Keys

link = "http://cedravium.ru/#/"


def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    go_to_registration_page(browser, 'test10', 'test62@mail.ru', 'qwerty11')
    sleep(1)
    go_to_home_page(browser)
    sleep(1)
    go_to_profile(browser)
    sleep(5)


def go_to_registration_page(browser, login, email, password):
    sign_up = browser.find_element(By.XPATH, "//button[@class='simple-button']")
    sign_up.click()
    login_form = browser.find_element(By.XPATH, "//form[@class='registration']//input[@type = 'text']")
    login_form.click()
    login_form.send_keys(login + Keys.TAB + email + Keys.TAB + password + Keys.TAB + password)
    button_register = browser.find_element(By.XPATH, "//form[@class='registration']//button[@type = 'submit']")
    button_register.click()


def go_to_home_page(browser):
    button_go_to_home_page = browser.find_element(By.CLASS_NAME, "simple-button")
    button_go_to_home_page.click()


def go_to_profile(browser):
    my_profile = browser.find_element(By.XPATH, "//a[@href='#/profile']")
    my_profile.click()


