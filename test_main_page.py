from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.common.keys import Keys


link = "http://cedravium.ru/#/"


def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    go_to_login_page(browser, 'test@mail.ru', 'qwerty11')
    sleep(1)
    go_to_home_page(browser)
    go_to_profile(browser)
    sleep(5)


def go_to_login_page(browser, mail, password):
    login_link = browser.find_element(By.CLASS_NAME, "simple-button")
    login_link.click()
    sign_in = browser.find_element(
        By.XPATH, "//form[@class='authentication']//input[@type = 'text']"
    )
    sign_in.click()
    sign_in.send_keys(mail + Keys.TAB + password + Keys.ENTER)


def go_to_home_page(browser):
    button_go_to_home_page = browser.find_element(By.CLASS_NAME, "simple-button")
    button_go_to_home_page.click()


def go_to_profile(browser):
    my_profile = browser.find_element(By.XPATH, "//a[@href='#/profile']")
    my_profile.click()


