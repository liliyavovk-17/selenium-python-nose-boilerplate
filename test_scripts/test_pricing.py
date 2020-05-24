from selenium import webdriver
from pages.pricing_page import PricingPage
import time


class TestPricing:

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.blueapron.com/pricing")

    def test_pricing_two_servings_module(self):
        pricing_page = PricingPage(self.driver)
        pricing_page.find_menu(2)
        pricing_page.assert_price_per_serving("9.99")
        pricing_page.assert_shipping_price("Free")
        pricing_page.assert_total_price("59.94")

    def test_pricing_change_two_serving_module(self):
        pricing_page = PricingPage(self.driver)
        time.sleep(3)
        pricing_page.change_recipes_amount(2)
        pricing_page.assert_price_per_serving("9.99")
        pricing_page.assert_shipping_price("7.99")
        pricing_page.assert_total_price("47.95")

    def test_pricing_four_serving_module(self):
        pricing_page = PricingPage(self.driver)
        pricing_page.find_menu(4)
        pricing_page.assert_price_per_serving("8.99")
        pricing_page.assert_shipping_price("Free")
        pricing_page.assert_total_price("71.92")

    def test_pricing_change_four_serving_module(self):
        pricing_page = PricingPage(self.driver)
        time.sleep(3)
        pricing_page.change_recipes_amount(3)
        pricing_page.assert_price_per_serving("7.99")
        # pricing_page.assert_shipping_price("7.99")
        pricing_page.assert_total_price("95.88")

    def test_click_select_button(self):
        pricing_page = PricingPage(self.driver)
        time.sleep(5)
        pricing_page.click_select_button()
        time.sleep(5)
        assert pricing_page.is_url_matches_sign_up_page(), "Title doesn't match."

    def tearDown(self):
        self.driver.close()
