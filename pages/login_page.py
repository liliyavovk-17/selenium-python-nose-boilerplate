from base_page import BasePage
from base_page import BasePageElement
from locators import LoginPageLocators


class EmailInputElement(BasePageElement):
    """This class gets the search text from the specified locator."""

    locator = LoginPageLocators.EMAIL_INPUT


class LoginPage(BasePage):
    """Login page action methods come here."""

    email_input = EmailInputElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Test" appears in page title."""
        return "Test" in self.driver.title

    def click_log_button(self):
        """Clicks the log in button."""
        element = self.driver.find_element(*LoginPageLocators.LOG_IN_BUTTON)
        element.click()
