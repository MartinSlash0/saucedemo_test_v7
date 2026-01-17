from pages.login_page import LoginPage
from pages.store_page import StorePage
from config import ConfigTest

def test_valid_login(driver):
    
    login_page = LoginPage(driver)
    store_page = StorePage(driver)
    # Opening Page
    login_page.open()
    # Verifying page open
    assert login_page.login_logo_is_visible(), "Page did not load"
    # Testing loging in with standard credentials
    login_page.login(
        ConfigTest.VALID_USERNAME,
        ConfigTest.VALID_PASSWORD
    )
    # Verifying login success
    assert store_page.app_logo_is_visible(), "Test failed!"