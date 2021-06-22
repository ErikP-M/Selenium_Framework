import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Pages.base_page import BasePage
from Resources.locators import CheckStepTwoPageElements


class CheckStepTwoPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def check_overview_step(self):
        label = self.find_text_in_element(CheckStepTwoPageElements.OVERVIEW_LABEL)
        return True if "OVERVIEW" in label else False

    def finish_checkout(self):
        self.click_on(CheckStepTwoPageElements.FINISH_BTN)
