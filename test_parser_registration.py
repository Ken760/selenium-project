#pytest -s -v --browser_name=chrome test_parser_registration.py
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.common.keys import Keys

link = "http://cedravium.ru/#/"


def test_registration(browser, login='test3', email='test54@mail.ru', password='qwerty11'):
    browser.get(link)
    browser.implicitly_wait(10)
    browser.get('http://cedravium.ru/#/')
    sign_up = browser.find_element(By.XPATH, "//button[@class='simple-button']")
    sign_up.click()
    sleep(0.5)
    login_form = browser.find_element(By.XPATH, "//form[@class='registration']//input[@type = 'text']")
    login_form.click()
    login_form.send_keys(login + Keys.TAB + email + Keys.TAB + password + Keys.TAB + password)
    button_register = browser.find_element(By.XPATH, "//form[@class='registration']//button[@type = 'submit']")
    button_register.click()
    sleep(2)
    button_go_to_home_page = browser.find_element(By.CLASS_NAME, 'simple-button')
    button_go_to_home_page.click()
    sleep(2)
    my_profile = browser.find_element(By.XPATH, "//a[@href='#/profile']")
    my_profile.click()
    sleep(2)


