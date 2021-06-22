import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Pages.base_page import BasePage
from Resources.locators import CartPageElements, HomePageElements


class CartPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def check_added_to_cart_items(self, dict_ids_to_check):
        self.click_on(HomePageElements.CART_BTN)
        in_cart_elements = self.driver.find_elements(*CartPageElements.IN_CART_ELEMENTS)
        matched_items = 0
        for key in dict_ids_to_check:
            for item in in_cart_elements:
                item_text = item.text.split('\n')[1].casefold()
                item_qty = int(item.text.split('\n')[0])
                if item_text.split()[-1] in key and dict_ids_to_check[key] == item_qty:
                    matched_items += 1
                    break
        if matched_items == len(in_cart_elements):
            return True
        else:
            return False

    def start_checkout(self):
        self.click_on(CartPageElements.CHECKOUT_BTN)
