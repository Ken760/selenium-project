from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def registration(login, email, password):
    try:
        driver = webdriver.Chrome()
        driver.get('http://cedravium.ru/#/')
        sign_up = driver.find_element(By.XPATH, "//button[@class='simple-button']")
        sign_up.click()
        time.sleep(0.5)
        login_form = driver.find_element(By.XPATH, "//form[@class='registration']//input[@type = 'text']")
        login_form.click()
        login_form.send_keys(login + Keys.TAB + email + Keys.TAB + password + Keys.TAB + password)
        time.sleep(1)
        button_register = driver.find_element(By.XPATH, "//form[@class='registration']//button[@type = 'submit']")
        button_register.click()
        time.sleep(1)
        button_go_to_home_page = driver.find_element(By.CLASS_NAME, 'simple-button')
        button_go_to_home_page.click()
        time.sleep(2)
        my_profile = driver.find_element(By.XPATH, "//a[@href='#/profile']")
        my_profile.click()

    finally:
        time.sleep(5)
        driver.quit()


registration('test2', 'test46@mail.ru', 'qwerty12')
