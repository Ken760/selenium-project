## Введите данные для регистрации
from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait

mail = 'test@mail.ru'
password = 'qwerty11'
##
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pytest

def regist():
    driver = webdriver.Chrome()
    driver.get('http://cedravium.ru/#/')
    sign_up = driver.find_element(By.XPATH, "//button[@class='simple-button']")
    time.sleep(0.5)
    sign_up.click()
    sign_in = driver.find_element(By.XPATH, "//form[@class='authentication']//input[@type = 'text']")
    sign_in.click()
    sign_in.send_keys(mail + Keys.TAB + password + Keys.ENTER)
    time.sleep(2)
    button_go_to_home_page = driver.find_element(By.CLASS_NAME, 'simple-button')
    button_go_to_home_page.click()

def cont():



