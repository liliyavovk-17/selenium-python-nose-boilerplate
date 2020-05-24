from base_page import BasePage
from locators import PricingPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PricingPageTwoServings(BasePage):

    def assert_two_serving_module_visible(self):
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".pom-PlanCard__contents"))
        )
        two_serving_module = self.driver.find_element(*PricingPageLocators.SERVING_2_SERVINGS_MODULE)
        two_serving_module.is_displayed()

    def assert_price_per_serving(self):
        two_serving_module_price_per_serving = self.driver.find_element(*PricingPageLocators.SERVING_2_COST_PER_SERVING)
        two_serving_module_price_per_serving.get_attribute("text")
        if "9.99" in str(two_serving_module_price_per_serving):
            return True

    def assert_shipping_price(self):
        two_serving_module_shipping_price = self.driver.find_element(*PricingPageLocators.SERVING_2_SHIPPING_PRICE)
        two_serving_module_shipping_price.get_attribute("text")
        if "FREE" in str(two_serving_module_shipping_price):
            return True

    def assert_total_price(self):
        two_serving_module_total_price = self.driver.find_element(*PricingPageLocators.SERVING_2_TOTAL_PRICE)
        two_serving_module_total_price.get_attribute("text")
        if "59.94" in str(two_serving_module_total_price):
            return True

    def change_recipes_to_two_two_serving(self):
        recipes_to_two = self.driver.find_element(*PricingPageLocators.SERVING_2_RECIPES_PER_WEEK_CHANGE)
        recipes_to_two.click()

    def wait_for_select_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(*PricingPageLocators.SELECT_BUTTON)
        )

    def click_select_button(self):
        select_button = self.driver.find_element(*PricingPageLocators.SELECT_BUTTON)
        select_button.click()

    def is_url_matches_sign_up_page(self):
        """Verifies hardcoded URL name matches current URL"""
        url = self.driver.current_url
        return "https://www.blueapron.com/users/sign_up" in url


class PricingPageTwoServingsAfterPriceChange(BasePage):

    def assert_price_per_serving(self):
        two_serving_module_price_per_serving = self.driver.find_element(*PricingPageLocators.SERVING_2_COST_PER_SERVING)
        two_serving_module_price_per_serving.get_attribute("text")
        if "9.99" in str(two_serving_module_price_per_serving):
            return True

    def assert_shipping_price(self):
        two_serving_module_shipping_price = self.driver.find_element(*PricingPageLocators.SERVING_2_SHIPPING_PRICE)
        two_serving_module_shipping_price.get_attribute("text")
        if "7.99" in str(two_serving_module_shipping_price):
            return True

    def assert_total_price(self):
        two_serving_module_total_price = self.driver.find_element(*PricingPageLocators.SERVING_2_TOTAL_PRICE)
        two_serving_module_total_price.get_attribute("text")
        if "47.95" in str(two_serving_module_total_price):
            return True