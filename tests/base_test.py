from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import unittest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.home_page import HomePage

class BaseTest(unittest.TestCase):
    """
    Base Test for each Test Case
    """
    def setUp(self):
        options = Options()
        self.driver = driver = webdriver.Remote(
                command_executor="http://localhost:4444",
                options=options
        )

        driver.get("http://16a.demofield.com/en/")
        driver.maximize_window()
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()