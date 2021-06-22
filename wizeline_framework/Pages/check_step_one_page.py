import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Pages.base_page import BasePage
from Resources.locators import CheckStepOnePageElements


class CheckStepOnePage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def fill_checkout_form(self, name, last_name, zip_code):
        self.enter_text(CheckStepOnePageElements.NAME_FIELD, name)
        self.enter_text(CheckStepOnePageElements.LAST_NAME_FIELD, last_name)
        self.enter_text(CheckStepOnePageElements.ZIP_CODE, zip_code)
        self.click_on(CheckStepOnePageElements.CONTINUE_BTN)
