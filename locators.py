from selenium.webdriver.common.by import By


class HomePageLocators(object):
    """A class for hoome page locators."""
    PRICING_IN_HEADER = (By.CSS_SELECTOR, ".header-nav .nav_pricing")


class PricingPageLocators(object):
    """A class for pricing page locators."""
    SERVING_2_SERVINGS_MODULE = (By.XPATH, "//h1[@class='pom-PlanCard__name'][contains(text(),'Signature')]")
    SERVING_2_COST_PER_SERVING = (By.XPATH, "//html/body/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div[3]/div/div/div/strong/span/span")
    SERVING_2_SHIPPING_PRICE = (By.XPATH, "//html/body/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div[3]/div/div/div[2]/strong")
    SERVING_2_TOTAL_PRICE = (By.XPATH, "//html/body/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div[3]/div/div[2]/div/h2/span/span")
    SERVING_2_RECIPES_PER_WEEK_CHANGE = (By.XPATH, "//html/body/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/div/ul/li/button")

    SERVING_4_SERVINGS_MODULE = (By.XPATH, "//h1[@class='pom-PlanCard__name'][contains(text(),'Signature for 4')]")
    SERVING_4_COST_PER_SERVING = (By.XPATH, "//html/body/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[3]/div/div/div/strong/span/span")
    SERVING_4_SHIPPING_PRICE = (By.XPATH, "//html/body/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[3]/div/div/div[2]/strong")
    SERVING_4_TOTAL_PRICE = (By.XPATH, "//html/body/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/h2/span/span")
    SERVING_4_RECIPES_PER_WEEK_CHANGE = (By.CSS_SELECTOR, ".purify_app-modules-react-app-common-plan-selector-PlanSelectorDesktop--_PlanSelectorDesktop-2uQp4 > div:nth-of-type(2) > div > div:nth-of-type(2) > div:nth-of-type(2) > div > ul > li:nth-of-type(2) > button")

    SELECT_BUTTON = (By.CLASS_NAME, "pom-Button--blue")


class SignUpPageLocators(object):
    """A class for sign up page locators."""
    APPLE_SIGN_UP_BUTTON = (By.ID, "appleid-signin")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".pom-Button--blue .pom-Button--mouseover")
    INVALID_EMAIL_ERROR_MESSAGE = (By.CSS_SELECTOR, ".pom-InputError")
