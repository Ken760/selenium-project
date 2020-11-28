from selenium.webdriver.common.by import By


class BasePageLocator():
    LOGIN_LINK = (By.XPATH, "//a[@href='#/auth']")
    HOME_PAGE = (By.CLASS_NAME, "simple-button")
    MY_PROFILE = (By.XPATH, "//a[@href='#/profile']")


class LoginPageLocators():
    SIGN_UP = (By.XPATH, "//a[@href='#/auth']")
    LOGIN_FORM = (By.CLASS_NAME, "authentication")
    REGISTER_FORM = (By.CLASS_NAME, "registration")
    EMAIL_INPUT_SIGN_IN = (By.XPATH, "//form[@class='authentication']//input[@type='text']")
    PASSWORD_INPUT_SIGN_IN = (By.XPATH, "//form[@class='authentication']//input[@type='password']")
    LOGIN_INPUT_SIGN_UP = (By.CSS_SELECTOR, "form.registration > div:nth-child(2) ")
    EMAIL_INPUT_SIGN_UP = (By.CSS_SELECTOR, "form.registration > div:nth-child(3) ")
    BUTTON_ENTER = (By.XPATH, "//form[@class='authentication']//button[@type = 'submit']")
    BUTTON_REGISTER = (By.XPATH, "//form[@class='registration']//button[@type = 'submit']")