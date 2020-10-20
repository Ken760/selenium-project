from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class CedraviumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://cedravium.ru/#/')

    # new user registration

    # def test_registration(self):
    #     driver = self.driver
    #     sign_up = driver.find_element(By.XPATH, "//button[@class='simple-button']")
    #     sign_up.click()
    #     time.sleep(0.5)
    #
    #     login_form = driver.find_element(By.XPATH, "//form[@class='registration']//input[@type = 'text']")
    #     login_form.click()
    #     login_form.send_keys('test' + Keys.TAB + 'test@mail.ru' + Keys.TAB + 'qwerty11' + Keys.TAB + 'qwerty11')
    #     time.sleep(1)
    #     button_register = driver.find_element(By.XPATH, "//form[@class='registration']//button[@type = 'submit']")
    #     button_register.click()
    #     time.sleep(5)

    # user authentication

    def test_sign_in(self):
        driver = self.driver
        sign_up = driver.find_element(By.XPATH, "//button[@class='simple-button']")
        sign_up.click()
        time.sleep(0.5)

        sign_in = driver.find_element(By.XPATH, "//form[@class='authentication']//input[@type = 'text']")
        sign_in.click()
        sign_in.send_keys('test@mail.ru' + Keys.TAB + 'qwerty11')
        time.sleep(0.5)
        button_authentication = driver.find_element(By.XPATH,
                                                    "//form[@class='authentication']//button[@type = 'submit']")
        button_authentication.click()
        time.sleep(1)

        button_go_to_home_page = driver.find_element(By.CLASS_NAME, 'simple-button')
        button_go_to_home_page.click()
        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
