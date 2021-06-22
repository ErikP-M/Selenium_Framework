import unittest
import sys
import os
from selenium import webdriver
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Resources.test_data import Urls
from Resources.test_data import Drivers


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(Drivers.CHROME_DRIVER)
        self.driver.get(Urls.URL_TO_TEST)

    def tearDown(self):
        self.driver.quit()
