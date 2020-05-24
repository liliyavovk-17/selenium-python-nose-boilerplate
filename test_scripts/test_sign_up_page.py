from selenium import webdriver
from pages.sign_up_page import SignUpPage


class TestSignUp:

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.blueapron.com/users/sign_up")

    def test_apple_id_button(self):
        sign_up_page = SignUpPage(self.driver)
        sign_up_page.verify_apple_button()

    def test_invalid_email(self):
        sign_up_page = SignUpPage(self.driver)
        sign_up_page.continue_with_invalid_email()

    def tearDown(self):
        self.driver.close()
