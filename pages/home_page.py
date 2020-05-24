from base_page import BasePage
from locators import HomePageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    """Home page action methods come here."""

    def is_url_matches_pricing_page(self):
        """Verifies hardcoded URL name matches current URL"""
        url = self.driver.current_url
        return "https://www.blueapron.com/pricing" in url

    def wait_for_nav_bar_element(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".header-nav .nav_pricing"))
        )

    def click_nav_bar_pricing(self):
        pricing_nav_bar = self.driver.find_element(*HomePageLocators.PRICING_IN_HEADER)
        pricing_nav_bar.click()
