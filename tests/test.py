from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest
from pages.home_page import HomePage


class BaseTest(unittest.TestCase):
    """
    Base Test for each Test Case
    """

    def setUp(self):
        options = Options()

        # stabilne flagi dla Docker + ARM VM
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--window-size=1920,1080")

        print("Creating Remote WebDriver")

        self.driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=options
        )

        print("Driver created")

        # timeout żeby test nie wisiał 5 minut
        self.driver.set_page_load_timeout(30)

        # implicit wait
        self.driver.implicitly_wait(5)

        print("Opening homepage")

        self.driver.get("http://16a.demofield.com/en/")

        self.driver.maximize_window()

        print("Page opened")

        # inicjalizacja Page Object
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        print("Closing browser")

        if self.driver:
            self.driver.quit()

        print("Browser closed")