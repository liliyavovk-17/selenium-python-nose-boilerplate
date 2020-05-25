from base_page import BasePage
from locators import PricingPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PricingPage(BasePage):
    """Pricing page action methods come here."""

    def find_menu(self, serving_amount):
        """Verifies Serving modules are displayed on the page."""
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".pom-PlanCard__contents"))
        )
        serving_module = None
        if serving_amount == 2:
            serving_module = self.driver.find_element(*PricingPageLocators.SERVING_2_SERVINGS_MODULE)
        elif serving_amount == 4:
            serving_module = self.driver.find_element(*PricingPageLocators.SERVING_4_SERVINGS_MODULE)
        return serving_module.is_displayed()

    def assert_price_per_serving(self, price_per_serving):
        """Verifies Serving modules prices per serving are correct."""
        text = None
        if price_per_serving == "9.99":
            two_serving_module_price_per_serving = self.driver.find_element(*PricingPageLocators.SERVING_2_COST_PER_SERVING)
            text = two_serving_module_price_per_serving.get_attribute("textContent")
        elif price_per_serving == "8.99" or price_per_serving == "7.99":
            four_serving_module_price_per_serving = self.driver.find_element(*PricingPageLocators.SERVING_4_COST_PER_SERVING)
            text = four_serving_module_price_per_serving.get_attribute("textContent")
        assert price_per_serving in str(text), "No such textContent"

    def assert_shipping_price(self, shipping_price):
        """Verifies Serving modules shipping prices are correct."""
        text = None
        text2 = None
        if shipping_price == "Free":
            two_serving_module_shipping_price = self.driver.find_element(*PricingPageLocators.SERVING_2_SHIPPING_PRICE)
            text = two_serving_module_shipping_price.get_attribute("textContent")
            four_serving_module_shipping_price = self.driver.find_element(*PricingPageLocators.SERVING_4_SHIPPING_PRICE)
            text2 = four_serving_module_shipping_price.get_attribute("textContent")
        elif shipping_price == "7.99":
            two_serving_module_shipping_price = self.driver.find_element(*PricingPageLocators.SERVING_2_SHIPPING_PRICE)
            text = two_serving_module_shipping_price.get_attribute("textContent")
            four_serving_module_price_per_serving = self.driver.find_element(*PricingPageLocators.SERVING_4_COST_PER_SERVING)
            text2 = four_serving_module_price_per_serving.get_attribute("textContent")
        assert shipping_price in str(text or text2), "No such textContent"

    def assert_total_price(self, total_price):
        """Verifies Serving modules total prices are correct."""
        text = None
        if total_price == "59.94" or total_price == "47.95":
            two_serving_module_total_price = self.driver.find_element(*PricingPageLocators.SERVING_2_TOTAL_PRICE)
            text = two_serving_module_total_price.get_attribute("textContent")
        elif total_price == "71.92" or total_price == "95.88":
            four_serving_module_total_price = self.driver.find_element(*PricingPageLocators.SERVING_4_TOTAL_PRICE)
            text = four_serving_module_total_price.get_attribute("textContent")
        assert total_price in str(text), "No such textContent"

    def change_recipes_amount(self, recipes_amount):
        """Clicks on the elements to change amount of recipes per week."""
        recipe_change = None
        if recipes_amount == 2:
            recipe_change = self.driver.find_element(*PricingPageLocators.SERVING_2_RECIPES_PER_WEEK_CHANGE)
        elif recipes_amount == 3:
            recipe_change = self.driver.find_element(*PricingPageLocators.SERVING_4_RECIPES_PER_WEEK_CHANGE)
        recipe_change.click()

    def wait_for_select_button(self):
        """Waits for Select button to load on the page."""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(*PricingPageLocators.SELECT_BUTTON)
        )

    def click_select_button(self):
        """Clicks Select button."""
        select_button = self.driver.find_element(*PricingPageLocators.SELECT_BUTTON)
        select_button.click()

    def is_url_matches_sign_up_page(self):
        """Verifies hardcoded URL name matches current URL"""
        url = self.driver.current_url
        return "https://www.blueapron.com/users/sign_up" in url
