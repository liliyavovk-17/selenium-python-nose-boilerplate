from base_page import BasePage
from locators import SignUpPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignUpPage(BasePage):
    """Sign Up page action methods come here."""

    def verify_apple_button(self):
        """Verifies Continue with Apple button is displayed on the page."""
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "appleid-signin"))
        )
        apple_id_button = self.driver.find_element(*SignUpPageLocators.APPLE_SIGN_UP_BUTTON)
        apple_id_button.is_displayed()

    def continue_with_invalid_email(self):
        """Verifies Invalid Email error message is displayed on the page."""
        continue_button = self.driver.find_element(*SignUpPageLocators.CONTINUE_BUTTON)
        continue_button.click()
        error_message = self.driver.find_element(*SignUpPageLocators.INVALID_EMAIL_ERROR_MESSAGE)
        error_message.is_displayed()
