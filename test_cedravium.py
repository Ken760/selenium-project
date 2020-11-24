## Данные для авторизации
mail = "test@mail.ru"
password = "qwerty11"
##
from allure_commons.types import Severity
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import allure
from random import choice
import string


def GenRandomLine(length=5, chars=string.ascii_lowercase + string.digits):
    return "".join([choice(chars) for i in range(length)])


class CedraviumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://cedravium.ru/#/")
        self.driver.maximize_window()

    @allure.title("Тестирование авторизации, созадния тестов")
    @allure.severity(Severity.BLOCKER)
    def test_cedravium(self):
        driver = self.driver
        with allure.step("Нажимаем кнопку Sign up"):
            sign_up = driver.find_element(By.CLASS_NAME, "simple-button")
            sign_up.click()

        sign_in = driver.find_element(
            By.XPATH, "//form[@class='authentication']//input[@type = 'text']"
        )
        sign_in.click()
        with allure.step(
            "Ожидаем ввода данных пользователя и нажимаем кнопку Enter для авторизации"
        ):
            sign_in.send_keys(mail + Keys.TAB + password + Keys.ENTER)

        with allure.step(
            "Проверяем успешность авторизации и возвращаемся на главную страницу"
        ):
            sleep(2)
            self.assertIn("All done, buddy", driver.page_source)
            button_go_to_home_page = driver.find_element(By.CLASS_NAME, "simple-button")
            button_go_to_home_page.click()

        with allure.step(
            "Проверяем наличие кнопки My profile и title на главной странице"
        ):
            self.assertIn("My profile" and "cedravium", driver.page_source)

        with allure.step("Открываем My profile"):
            my_profile = driver.find_element(By.XPATH, "//a[@href='#/profile']")
            my_profile.click()
            sleep(2)

        with allure.step("Ищем логин пользователя на страницы профиля"):
            self.assertTrue(driver.find_element(By.CSS_SELECTOR, "h2"))

        with allure.step("Нажимаем кнопку создания теста "):
            Button_create_test = driver.find_element(By.CLASS_NAME, "simple-button")
            Button_create_test.click()
            sleep(2)
        with allure.step("Заполняем созданый тест данными"):
            title_test = driver.find_element(
                By.CLASS_NAME, "constructor-page__test-name"
            )
            title_test.send_keys("Test" + Keys.TAB + Keys.ENTER)
            My_description = driver.find_element(By.XPATH, "//textarea")
            My_description.send_keys(GenRandomLine(500))
            Button_add = driver.find_element(By.XPATH, "//button")
            Button_add.click()
            sleep(2)
            Radio_button = driver.find_element(By.XPATH, "//li[1]")
            Radio_button.click()
            sleep(2)
            Question = driver.find_element(
                By.XPATH, "//input[@class='question__title']"
            ).send_keys("qwerty1234567890")
        with allure.step("Добавления Option"):
            transparent = driver.find_element(By.CLASS_NAME, "transparent")
            while True:
                transparent.click()
                sleep(2)
                transparent.click()
                break
            sleep(2)

        with allure.step("Заполнения всех полей Option рандомными значениями"):
            Option = driver.find_elements(
                By.XPATH, "//input[@class='question__answer']"
            )
            for Options in Option:
                Options.send_keys(GenRandomLine())

        with allure.step("Закрыть один вопрос и выбрать вариант ответа"):
            close = driver.find_element(
                By.XPATH, '//*[@id="question-0"]/div[2]/div[4]/span'
            )
            close.click()
            radio_button = driver.find_element(
                By.XPATH, "//*[@id='question-0']/div[2]/div[2]/label"
            )
            radio_button.click()
            sleep(2)

        with allure.step("Нажимаем create test и возвращаемся на главную страницу"):
            button_create = driver.find_element(By.CLASS_NAME, "create-test")
            button_create.click()
            sleep(2)
            button_go_to_home_page = driver.find_element(By.CLASS_NAME, "simple-button")
            button_go_to_home_page.click()
            sleep(1)

        with allure.step("Возвращаемся в профиль нажимаем Edit и удаляем созданный тест"):
            Mp = my_profile.click()
            sleep(1)
            self.assertTrue(driver.find_element(By.CLASS_NAME, 'home-page__tests-list__test'))
            button_edit = driver.find_element(By.LINK_TEXT, "Edit")
            button_edit.click()
            sleep(1)
            self.assertIn('Delete test', driver.page_source)
            button_delete = driver.find_element(
                By.XPATH, "//button[@class='simple-button negative']"
            )
            button_delete.click()
            sleep(1)
            button_go_to_home_page = driver.find_element(By.CLASS_NAME, "simple-button")
            button_go_to_home_page.click()
            sleep(1)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
