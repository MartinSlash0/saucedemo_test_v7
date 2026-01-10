from pages.login_page import LoginPage
from config import ConfigTest

def test_valid_login(driver):
    
    login_page = LoginPage(driver)
    # Opening Page
    login_page.open()
    # Testing loging in with standard credentials
    login_page.login(
        ConfigTest.INVALID_USERNAME,
        ConfigTest.INVALID_PASSWORD
    )
    # Verifying login success
    assert login_page.is_cred_invalid()