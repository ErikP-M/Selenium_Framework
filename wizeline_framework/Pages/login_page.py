import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Pages.base_page import BasePage
from Resources.locators import LoginPageElements, HomePageElements


class LoginPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def login(self, user, password):
        self.driver.find_element(*LoginPageElements.USR_BOX).clear()
        self.enter_text(LoginPageElements.USR_BOX, user)
        self.enter_text(LoginPageElements.PASS_BOX, password)
        self.click_on(LoginPageElements.LOGIN_BTN)

    def successful_login(self, txt_to_find):
        text_element = self.find_text_in_element(HomePageElements.PROD_LABEL)
        return True if txt_to_find == text_element else False

    def unsuccessful_login(self):
        return self.find_text_in_element(LoginPageElements.ERROR_LOGIN_MSG)
