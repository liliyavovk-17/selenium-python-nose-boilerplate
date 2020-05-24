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
        text = two_serving_module_price_per_serving.get_attribute("textContent")
        assert "9.99" in str(text), "No such textContent"

    def assert_shipping_price(self):
        two_serving_module_shipping_price = self.driver.find_element(*PricingPageLocators.SERVING_2_SHIPPING_PRICE)
        text = two_serving_module_shipping_price.get_attribute("textContent")
        assert "Free" in str(text), "No such textContent"

    def assert_total_price(self):
        two_serving_module_total_price = self.driver.find_element(*PricingPageLocators.SERVING_2_TOTAL_PRICE)
        text = two_serving_module_total_price.get_attribute("textContent")
        assert "59.94" in str(text), "No such textContent"


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

    def change_recipes_to_two_two_serving(self):
        recipes_to_two = self.driver.find_element(*PricingPageLocators.SERVING_2_RECIPES_PER_WEEK_CHANGE)
        recipes_to_two.click()

    def assert_price_per_serving(self):
        two_serving_module_price_per_serving = self.driver.find_element(*PricingPageLocators.SERVING_2_COST_PER_SERVING)
        text = two_serving_module_price_per_serving.get_attribute("textContent")
        assert "9.99" in str(text), "No such textContent"

    def assert_shipping_price(self):
        two_serving_module_shipping_price = self.driver.find_element(*PricingPageLocators.SERVING_2_SHIPPING_PRICE)
        text = two_serving_module_shipping_price.get_attribute("textContent")
        assert "7.99" in str(text), "No such textContent"

    def assert_total_price(self):
        two_serving_module_total_price = self.driver.find_element(*PricingPageLocators.SERVING_2_TOTAL_PRICE)
        text = two_serving_module_total_price.get_attribute("textContent")
        assert "47.95" in str(text), "No such textContent"


class PricingPagFourServings(BasePage):

    def assert_four_serving_module_visible(self):
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".pom-PlanCard__contents"))
        )
        four_serving_module = self.driver.find_element(*PricingPageLocators.SERVING_4_SERVINGS_MODULE)
        four_serving_module.is_displayed()

    def assert_price_per_serving(self):
        two_serving_module_price_per_serving = self.driver.find_element(*PricingPageLocators.SERVING_2_COST_PER_SERVING)
        text = two_serving_module_price_per_serving.get_attribute("textContent")
        assert "9.99" in str(text), "No such textContent"

    def assert_shipping_price(self):
        four_serving_module_shipping_price = self.driver.find_element(*PricingPageLocators.SERVING_4_SHIPPING_PRICE)
        text = four_serving_module_shipping_price.get_attribute("textContent")
        assert "Free" in str(text), "No such textContent"

    def assert_total_price(self):
        four_serving_module_total_price = self.driver.find_element(*PricingPageLocators.SERVING_4_TOTAL_PRICE)
        text = four_serving_module_total_price.get_attribute("textContent")
        assert "71.92" in str(text), "No such textContent"


class PricingPageFourServingsAfterPriceChange(BasePage):

    def change_recipes_to_three_four_serving(self):
        recipes_to_three = self.driver.find_element(*PricingPageLocators.SERVING_4_RECIPES_PER_WEEK_CHANGE)
        recipes_to_three.click()

    def assert_price_per_serving(self):
        four_serving_module_price_per_serving = self.driver.find_element(*PricingPageLocators.SERVING_4_COST_PER_SERVING)
        text = four_serving_module_price_per_serving.get_attribute("textContent")
        assert "7.99" in str(text), "No such textContent"

    # def assert_shipping_price(self):
    #     four_serving_module_shipping_price = self.driver.find_element(*PricingPageLocators.SERVING_4_SHIPPING_PRICE)
    #     text = four_serving_module_shipping_price.get_attribute("textContent")
    #     assert "7.99" in str(text), "No such textContent"

    def assert_total_price(self):
        four_serving_module_total_price = self.driver.find_element(*PricingPageLocators.SERVING_4_TOTAL_PRICE)
        text = four_serving_module_total_price.get_attribute("textContent")
        assert "95.88" in str(text), "No such textContent"
