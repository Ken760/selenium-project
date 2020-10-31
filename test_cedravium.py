## Данные для авторизации
mail = 'test@mail.ru'
password = 'qwerty11'
##
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
        self.driver.maximize_window()

    @allure.title('Тестирование авторизации, созадния, открытия тестов')
    @allure.severity(Severity.BLOCKER)
    def test_cedravium(self):
        driver = self.driver
        with allure.step('Нажимаем кнопку Sign up'):
            sign_up = driver.find_element(By.XPATH, "//button[@class='simple-button']")
            time.sleep(0.5)
            sign_up.click()

        sign_in = driver.find_element(By.XPATH, "//form[@class='authentication']//input[@type = 'text']")
        sign_in.click()
        with allure.step('Ожидаем ввода данных пользователя и нажимаем кнопку Enter для авторизации'):
            sign_in.send_keys(mail + Keys.TAB + password + Keys.ENTER)
            time.sleep(1)

        with allure.step('Проверяем успешность авторизации и возвращаемся на главную страницу'):
            time.sleep(2)
            assert 'All done, buddy' in driver.page_source
            button_go_to_home_page = driver.find_element(By.CLASS_NAME, 'simple-button')
            button_go_to_home_page.click()
            time.sleep(2)

        with allure.step('Проверяем наличие кнопки My profile и title на главной странице'):
            assert 'My profile' in driver.page_source and 'cedravium' in driver.title

        with allure.step('Открываем My profile'):
            my_profile = driver.find_element(By.XPATH, "//a[@href='#/profile']")
            my_profile.click()
            time.sleep(2)

        with allure.step('Ищем логин пользователя на страницы профиля'):
            assert driver.find_element(By.CSS_SELECTOR, '#app > main > div > section.profile-page__header > h2')

        Button_create_test = driver.find_element(By.CLASS_NAME, 'simple-button').click()
        time.sleep(2)
        title_test = driver.find_element(By.CLASS_NAME, 'constructor-page__test-name')
        title_test.send_keys('Test' + Keys.TAB + Keys.ENTER)
        My_description = driver.find_element(By.XPATH, '//textarea').send_keys('test 1234567890 !@#$%^&*()_+|?><,')
        Button_add = driver.find_element(By.XPATH, '//button')
        Button_add.click()
        time.sleep(2)
        Radio_button = driver.find_element(By.XPATH, '//li[1]').click()
        time.sleep(2)
        Question = driver.find_element(By.XPATH, "//input[@class='question__title']").send_keys('qwerty1234567890')
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__test_cedravium__':
    unittest.test_cedravium()
