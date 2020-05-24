from selenium import webdriver
from pages.home_page import HomePage
from pages.pricing_page import PricingPage
import time


class TestNavigation:

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.blueapron.com")

    def test_landing_on_pricing_page(self):
        home_page = HomePage(self.driver)
        home_page.wait_for_nav_bar_element()
        home_page.click_nav_bar_pricing()
        time.sleep(10)
        pricing_page = PricingPage(self.driver)
        pricing_page.find_menu(2)
        assert home_page.is_url_matches_pricing_page(), "Title doesn't match."

    def tearDown(self):
        self.driver.close()
