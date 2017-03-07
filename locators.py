from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    """A class for login page locators."""
    EMAIL_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOG_IN_BUTTON = (By.CSS_SELECTOR, "button.login-button")
    FORGOT_PASSWORD_BUTTON = (By.CLASS_NAME, "forgot-password")
