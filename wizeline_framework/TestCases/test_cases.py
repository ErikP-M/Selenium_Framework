import unittest
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Pages.login_page import LoginPage
from Pages.home_page import HomePage
from Pages.cart_page import CartPage
from Pages.check_step_one_page import CheckStepOnePage
from Pages.checkout_step_two_page import CheckStepTwoPage
from Pages.checkout_complete_page import CheckoutCompletePage
from TestCases.base_test import BaseTest
from Resources.test_data import Credentials, TextStr
from Resources.locators import HomePageElements


class TestCases(BaseTest):

    def setUp(self):
        super().setUp()
        self.login_ins = LoginPage(self.driver)
        self.home_ins = HomePage(self.driver)
        self.cart_ins = CartPage(self.driver)
        self.check_ins = CheckStepOnePage(self.driver)
        self.check_two_ins = CheckStepTwoPage(self.driver)
        self.check_complete_ins = CheckoutCompletePage(self.driver)

    def test_01_login_successfully(self):
        self.login_ins.login(Credentials.VALID_USR, Credentials.VALID_PASS)
        self.assertTrue(self.login_ins.successful_login(TextStr.SUCCESS_LOGIN_TXT), TextStr.FAILED_TXT)

    def test_02_invalid_user(self):
        self.login_ins.login(Credentials.INVALID_USR, Credentials.VALID_PASS)
        self.assertIn(TextStr.INVALID_USR_TXT, self.login_ins.unsuccessful_login(), TextStr.FAILED_TXT)

    def test_03_logout_home_page(self):
        self.login_ins.login(Credentials.VALID_USR, Credentials.VALID_PASS)
        self.assertTrue(self.login_ins.successful_login(TextStr.SUCCESS_LOGIN_TXT), TextStr.FAILED_TXT)
        self.home_ins.logout()
        self.assertTrue(self.home_ins.successful_logout(), TextStr.FAILED_TXT)

    def test_04_sort_prod_by_price_low_high(self):
        self.login_ins.login(Credentials.VALID_USR, Credentials.VALID_PASS)
        self.assertTrue(self.login_ins.successful_login(TextStr.SUCCESS_LOGIN_TXT), TextStr.FAILED_TXT)
        self.home_ins.sort_prod_price_low_high()
        self.assertTrue(self.home_ins.check_sorted_prods_price_low_to_high(), TextStr.FAILED_TXT)
    
    def test_05_add_items_to_shopping_cart(self):
        self.login_ins.login(Credentials.VALID_USR, Credentials.VALID_PASS)
        self.assertTrue(self.login_ins.successful_login(TextStr.SUCCESS_LOGIN_TXT), TextStr.FAILED_TXT)
        dict_added_ids = self.home_ins.add_random_items_to_cart(3)  # Number of random items to add
        self.assertTrue(self.cart_ins.check_added_to_cart_items(dict_added_ids), TextStr.FAILED_TXT)
    
    def test_06_add_specific_prod_to_cart(self):
        self.login_ins.login(Credentials.VALID_USR, Credentials.VALID_PASS)
        self.assertTrue(self.login_ins.successful_login(TextStr.SUCCESS_LOGIN_TXT), TextStr.FAILED_TXT)
        self.home_ins.add_product_to_cart(HomePageElements.ADD_CART_BTN_ONESIE)
        dict_added_id = {"add-to-cart-sauce-labs-onesie": 1}
        self.assertTrue(self.cart_ins.check_added_to_cart_items(dict_added_id), TextStr.FAILED_TXT)

    def test_07_complete_purchase(self):
        self.login_ins.login(Credentials.VALID_USR, Credentials.VALID_PASS)
        self.assertTrue(self.login_ins.successful_login(TextStr.SUCCESS_LOGIN_TXT), TextStr.FAILED_TXT)
        dict_added_ids = self.home_ins.add_random_items_to_cart(1)  # Number of random items to add
        self.assertTrue(self.cart_ins.check_added_to_cart_items(dict_added_ids), TextStr.FAILED_TXT)
        self.cart_ins.start_checkout()
        self.check_ins.fill_checkout_form(Credentials.NAME, Credentials.LAST_NAME, Credentials.ZIP_CODE)
        self.assertTrue(self.check_two_ins.check_overview_step(), TextStr.FAILED_TXT)
        self.check_two_ins.finish_checkout()
        self.assertTrue(self.check_complete_ins.validate_complete_checkout())

    def tearDown(self):
        super().tearDown()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reports',
                                                           report_title='SWAG LABS test report ',
                                                           report_name='Test_Report'))

