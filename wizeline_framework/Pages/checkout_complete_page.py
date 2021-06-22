import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Pages.base_page import BasePage
from Resources.locators import CheckoutCompleteElements


class CheckoutCompletePage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def validate_complete_checkout(self):
        label = self.find_text_in_element(CheckoutCompleteElements.COMPLETE_LABEL)
        return True if "COMPLETE" in label else False
