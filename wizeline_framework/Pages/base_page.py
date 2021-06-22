from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_cond


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_on(self, locator):
        WebDriverWait(self.driver, 10).until(exp_cond.visibility_of_element_located(locator)).click()

    def enter_text(self, locator, text):
        WebDriverWait(self.driver, 10).until(exp_cond.visibility_of_element_located(locator)).send_keys(text)

    def find_text_in_element(self, locator):
        return WebDriverWait(self.driver, 10).until(exp_cond.visibility_of_element_located(locator)).text

    def is_element_visible(self, locator):
        element = WebDriverWait(self.driver, 10).until(exp_cond.visibility_of_element_located(locator))
        return bool(element)
