from selenium import webdriver
import unittest

driver = webdriver.Chrome()

driver.get('http://cedravium.ru/#/')
assert "cedravium" in driver.page_source
