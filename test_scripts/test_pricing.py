from selenium import webdriver
from pages.pricing_page import PricingPageTwoServings
from pages.pricing_page import PricingPageTwoServingsAfterPriceChange
from pages.pricing_page import PricingPagFourServings
from pages.pricing_page import PricingPageFourServingsAfterPriceChange
import time


class TestPricing:

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.blueapron.com/pricing")

    def test_pricing_two_servings_module(self):
        pricing_page = PricingPageTwoServings(self.driver)
        pricing_page.assert_two_serving_module_visible()
        pricing_page.assert_price_per_serving()
        pricing_page.assert_shipping_price()
        pricing_page.assert_total_price()

    def test_pricing_change_two_serving_module(self):
        pricing_page_price_change = PricingPageTwoServingsAfterPriceChange(self.driver)
        time.sleep(3)
        pricing_page_price_change.change_recipes_to_two_two_serving()
        pricing_page_price_change.assert_price_per_serving()
        pricing_page_price_change.assert_shipping_price()
        pricing_page_price_change.assert_total_price()

    def test_pricing_four_serving_module(self):
        pricing_page = PricingPagFourServings(self.driver)
        pricing_page.assert_four_serving_module_visible()
        pricing_page.assert_price_per_serving()
        pricing_page.assert_shipping_price()
        pricing_page.assert_total_price()

    def test_pricing_change_four_serving_module(self):
        pricing_page = PricingPageFourServingsAfterPriceChange(self.driver)
        time.sleep(3)
        pricing_page.change_recipes_to_three_four_serving()
        pricing_page.assert_price_per_serving()
        # pricing_page.assert_shipping_price()
        pricing_page.assert_total_price()

    def test_click_select_button(self):
        pricing_page = PricingPageTwoServings(self.driver)
        time.sleep(5)
        pricing_page.click_select_button()
        assert pricing_page.is_url_matches_sign_up_page(), "Title doesn't match."

    def tearDown(self):
        self.driver.close()
