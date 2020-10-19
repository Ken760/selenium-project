from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class CedraviumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://cedravium.ru/#/')

    def test_registration(self):
        driver = self.driver
        sign_up = driver.find_element(By.XPATH, "//button[@class='simple-button']")
        sign_up.click()
        time.sleep(0.5)

        login_form = driver.find_element(By.XPATH, "//form[@class='registration']//input[@type = 'text']")
        login_form.click()
        login_form.send_keys('ken760' + Keys.TAB + 'nehnaev@bk.ru' + Keys.TAB + 'qwerty1' + Keys.TAB + 'qwerty1')
        time.sleep(2)
        button_register = driver.find_element(By.XPATH, "//form[@class='registration']//button[@type = 'submit']")
        button_register.click()
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
