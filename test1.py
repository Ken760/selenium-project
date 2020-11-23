from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import unittest


class CTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://cedravium.ru/#/")

    def test_regist(self):
        driver = self.driver
        driver.get("http://cedravium.ru/#/")
        sign_up = driver.find_element(By.XPATH, "//button[@class='simple-button']")
        sleep(0.5)
        sign_up.click()
        sign_in = driver.find_element(By.XPATH, "//form[@class='authentication']//input[@type = 'text']")
        sign_in.click()
        sign_in.send_keys(mail + Keys.TAB + password + Keys.ENTER)
        sleep(2)
        button_go_to_home_page = driver.find_element(By.CLASS_NAME, 'simple-button')
        button_go_to_home_page.click()


if __name__ == "__main__":
    unittest.main()
