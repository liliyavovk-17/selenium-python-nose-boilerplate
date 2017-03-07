from selenium import webdriver
from pages.login_page import LoginPage


class TestLogin:

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.test.com")

    def test_something(self):
        login_page = LoginPage(self.driver)
        assert login_page.is_title_matches(), "Title doesn't match."
        login_page.email_input = "hentest@test.com"
        email_input_text = login_page.email_input
        assert email_input_text == "hentest@test.com", "Some error message."

    def tearDown(self):
        self.driver.close()
