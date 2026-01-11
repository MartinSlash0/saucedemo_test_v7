from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import ConfigTest

class BasePage():
    
    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, ConfigTest.WAIT_TIME_SHORT)

    def wait_for_presence(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )
    
    def wait_for_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )