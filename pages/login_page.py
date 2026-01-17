from config import ConfigTest
from pages.base_page import BasePage
from locators import LocatorsLogInPage
from locators import LocatorsStorePage

class LoginPage(BasePage):

    def open(self):
        # Opening page
        self.driver.get(ConfigTest.BASE_URL)

    def login(self, username, password):
        # Finding username field element
        username_field = self.wait_for_presence(LocatorsLogInPage.USER_NAME_FIELD)
        # Finding password field element
        password_field = self.wait_for_presence(LocatorsLogInPage.PASSWORD_FIELD)
        # Finding login button element
        login_button = self.wait_for_clickable(LocatorsLogInPage.LOGIN_BUTTON)
        # Writing username info in field
        username_field.send_keys(username)
        # Writing password info in field
        password_field.send_keys(password)
        # Clicking button
        login_button.click()
    
    def login_logo_is_visible(self):
        #Verify page loading
        login_logo = self.wait_for_presence(LocatorsLogInPage.LOGIN_LOGO)
        return login_logo.is_displayed()
    
    def is_cred_invalid(self):
        # Verifying login was denied
        error = self.wait_for_presence(LocatorsLogInPage.ERROR_PROMPT)
        return error.is_displayed()