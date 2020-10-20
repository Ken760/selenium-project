from allure_commons.types import Severity
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import allure


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

    @allure.title('Авторизация пользователя')
    @allure.severity(Severity.BLOCKER)
    def test_sign_in(self):
        driver = self.driver
        with allure.step('Нажимаем кнопку Sign up'):
            sign_up = driver.find_element(By.XPATH, "//button[@class='simple-button']")
            sign_up.click()
            time.sleep(0.5)

        sign_in = driver.find_element(By.XPATH, "//form[@class='authentication']//input[@type = 'text']")
        sign_in.click()
        with allure.step('Ожидаем ввода данных пользователя'):
            sign_in.send_keys('test@mail.ru' + Keys.TAB + 'qwerty11')
            time.sleep(0.5)
        with allure.step('Нажимает кнопку авторизации'):
            button_authentication = driver.find_element(By.XPATH,
                                                        "//form[@class='authentication']//button[@type = 'submit']")
            button_authentication.click()
            time.sleep(1)

        with allure.step('Возвращаемся на главную страницу'):
            button_go_to_home_page = driver.find_element(By.CLASS_NAME, 'simple-button')
            button_go_to_home_page.click()
            time.sleep(2)

        with allure.step('Проверяем title главной страницы'):
            assert driver.title == 'cedravium'


if __name__ == '__test_cedravium__':
    unittest.test_cedravium()
