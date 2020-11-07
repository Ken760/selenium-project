from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest


class TestTask(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_yandex_search(self):
        driver = self.driver
        driver.get('https://yandex.ru/')
        data_input = driver.find_element(By.ID, 'text')
        data_input.send_keys('')
        time.sleep(3)
        suggest = driver.find_element(By.CLASS_NAME, 'mini-suggest__popup_visible')
        assert suggest
        print('Проверка таблицы с подсказками')
        data_input.send_keys(Keys.ENTER)
        time.sleep(2)
        assert 'https://tensor.ru/' in driver.page_source
        print('Ссылка на официальный сайт присутсвтует на странице')


    def test_yandex_picture(self):
        driver = self.driver
        driver.get('https://yandex.ru/')
        yandex_pictures = driver.find_element(By.LINK_TEXT, "Картинки")
        assert yandex_pictures
        yandex_pictures.click()
        tabs = driver.window_handles  # список
        driver.switch_to.window(tabs[1])
        search = driver.find_element(By.CLASS_NAME, 'PopularRequestList-Shadow')
        search.click()
        time.sleep(1)
        img1 = driver.find_element(By.CLASS_NAME, 'serp-item__link')
        img1.click()
        assert img1
        print('Изображение появилось')
        time.sleep(2)
        img1.send_keys(Keys.ARROW_RIGHT)
        time.sleep(2)
        img1.send_keys(Keys.ARROW_LEFT)
        assert img1
        print('Изображение совпадает')
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__testtask__':
    unittest.testtask()
