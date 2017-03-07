from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):

    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __set__(self, obj, value):
        """Sets the text to the value supplied."""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator))
        driver.find_element(*self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object."""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator))
        element = driver.find_element(*self.locator)
        return element.get_attribute("value")
