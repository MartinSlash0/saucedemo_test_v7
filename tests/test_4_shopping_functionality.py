from pages.store_page import StorePage
from pages.login_page import LoginPage
from config import ConfigTest

def test_shopping_cart(driver):
    login_page = LoginPage(driver)
    store_page = StorePage(driver)
    #Loading page
    login_page.open()
    #Verifying page open
    assert login_page.login_logo_is_visible, "Page did not load!"
    #Login
    login_page.login(
        ConfigTest.VALID_USERNAME,
        ConfigTest.VALID_PASSWORD
    )
    # Verifying login success
    assert store_page.app_logo_is_visible(), "Failed to login!"
    # Adding item to cart
    store_page.add_item_to_cart()
    # Opening shopping cart
    store_page.open_shopping_cart()
    # Verifying if item in cart success
    assert store_page.is_in_cart(), "Failed to open cart!"
