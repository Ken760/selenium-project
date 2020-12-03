from selenium.webdriver.common.by import By


class BasePageLocators():
    SIGN_UP_LINK = (By.XPATH, "//a[@href='#/auth']")
    HOME_PAGE = (By.CLASS_NAME, "simple-button")
    MY_PROFILE = (By.XPATH, "//a[@href='#/profile']")


class LoginPageLocators():
    SIGN_UP = (By.XPATH, "//a[@href='#/auth']")
    LOGIN_FORM = (By.CLASS_NAME, "authentication")
    REGISTER_FORM = (By.CLASS_NAME, "registration")
    EMAIL_INPUT_SIGN_IN = (By.XPATH, "//form[@class='authentication']//input[@type='text']")
    PASSWORD_INPUT_SIGN_IN = (By.XPATH, "//form[@class='authentication']//input[@type='password']")
    LOGIN_INPUT_SIGN_UP = (By.CSS_SELECTOR, "form.registration > div:nth-child(2) > input[type=text]")
    EMAIL_INPUT_SIGN_UP = (By.CSS_SELECTOR, "form.registration > div:nth-child(3) > input[type=text]")
    PASSWORD_INPUT_SIGN_UP = (By.CSS_SELECTOR, "form.registration > div:nth-child(4) > input[type=password]")
    CONFIRM_PASSWORD_INPUT_SIGN_UP = (By.CSS_SELECTOR, "form.registration > div:nth-child(5) > input[type=password]")
    BUTTON_ENTER = (By.XPATH, "//form[@class='authentication']//button[@type = 'submit']")
    BUTTON_REGISTER = (By.XPATH, "//form[@class='registration']//button[@type = 'submit']")


class CreateTest():
    BUTTON_CREATE_TEST = (By.CLASS_NAME, "simple-button")
    TITLE_TEST = (By.CLASS_NAME, "constructor-page__test-name")
    BUTTON_ADD_DESCRIPTION = (By.XPATH, "//div[@class='constructor-page__main-panel']//button[@class='simple-button']")
    INPUT_MY_DESCRIPTION = (By.XPATH, "//textarea")
    BUTTON_ADD_TEST = (By.CLASS_NAME, "simple-button circle")
    TEST_ONE_OF_THE_LIST = (By.XPATH, "//li[@data_question_type='RADIO_BUTTON']")
    TEST_SEVERAL_OF_THE_LIST = (By.XPATH, "//li[@data_question_type='CHECK_BOX']")
    TEST_TEXT_INPUT = (By.XPATH, "//li[@data_question_type='INPUT_FIELD']")
