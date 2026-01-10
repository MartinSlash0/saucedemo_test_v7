from pages.login_page import LoginPage
from config import ConfigTest

def test_valid_login(driver):
    
    login_page = LoginPage(driver)
    # Opening Page
    login_page.open()
    # Testing loging in with standard credentials
    login_page.login(
        ConfigTest.VALID_USERNAME,
        ConfigTest.VALID_PASSWORD
    )
    # Verifying login success
    assert login_page.is_logged_in()