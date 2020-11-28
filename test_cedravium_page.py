from pages.cedravium_page import LoginPage
import time

def test_login(browser):
    link = 'http://cedravium.ru/#/'
    login = LoginPage(browser, link)
    login.open()
    login.should_be_login_url()
    time.sleep(2)
