from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.create_account_page import CreateAccountPage

class Locators:
    CREATE_ACCOUNT_EMAIL = (By.ID, "email_create")
    CREATE_ACCOUNT_BUTTON = (By.ID, "SubmitCreate")

class AuthenticationPage(BasePage):
    def enter_create_account_email(self, email):
        self.driver.find_element(*Locators.CREATE_ACCOUNT_EMAIL).send_keys(email)

    def click_create_account(self):
        self.driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()
        return CreateAccountPage(self.driver)