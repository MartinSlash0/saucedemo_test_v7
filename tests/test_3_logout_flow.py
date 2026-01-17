from pages.login_page import LoginPage
from pages.store_page import StorePage
from config import ConfigTest

def test_logout(driver):
    login_page = LoginPage(driver)
    store_page = StorePage(driver)
    #Opening page
    login_page.open()
    assert login_page.login_logo_is_visible(), "Page did not load!"
    #Login
    login_page.login(
        ConfigTest.VALID_USERNAME,
        ConfigTest.VALID_PASSWORD
    )
    #Verifying login
    assert store_page.app_logo_is_visible(), "Failed login!"
    #Opening sidebar
    store_page.open_sidebar()
    #Logging out
    store_page.logout()
    #Verifying logout
    assert login_page.login_logo_is_visible(), "Failed to logout!"
