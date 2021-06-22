import random
import sys
import os
from collections import Counter
from selenium.webdriver.common.by import By
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Pages.base_page import BasePage
from Resources.locators import HomePageElements, LoginPageElements


class HomePage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def logout(self):
        self.click_on(HomePageElements.BAR_BTN)
        self.click_on(HomePageElements.LOGOUT_BTN)

    def successful_logout(self):
        return True if self.is_element_visible(LoginPageElements.LOGIN_BTN) else False

    def sort_prod_price_low_high(self):
        self.click_on(HomePageElements.DROP_BAR)
        self.click_on(HomePageElements.SORT_PRICE_LH)

    def check_sorted_prods_price_low_to_high(self):
        prices = self.driver.find_elements(*HomePageElements.PRICES)
        inter_prices = [float(price.text.split("$")[-1]) for price in prices]
        return True if sorted(inter_prices) == inter_prices else False

    def add_random_items_to_cart(self, num_of_items):
        element_btns = self.driver.find_elements(*HomePageElements.ADD_TO_CART_BTN)
        btns_ids = [btn_id.get_attribute("id") for btn_id in element_btns]
        add_to_cart_btn_ids = [idx for idx in btns_ids if "add-to-cart" in idx]
        selected_ids = random.sample(add_to_cart_btn_ids, num_of_items)
        for add_cart_id in selected_ids:
            self.click_on((By.ID, "{}".format(add_cart_id)))
        return Counter(selected_ids)

    def add_product_to_cart(self, add_btn_locator):
        self.click_on(add_btn_locator)
