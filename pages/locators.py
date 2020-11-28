from selenium.webdriver.common.by import By

class BasePageLocator():
    LOGIN_LINK = (By.XPATH, "//a[@href='#/auth']")
    LOGIN_LINK_INVALID = (By.XPATH, "//a[@href='#/auth_invalid']")

class LoginPageLocators():
    SIGN_UP = (By.XPATH, "//a[@href='#/auth']")
    LOGIN_FORM = (By.CLASS_NAME, "authentication")
    REGISTER_FORM = (By.CLASS_NAME, "registration")
