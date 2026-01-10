from pages.store_page import StorePage
from pages.login_page import LoginPage
from config import ConfigTest

def test_checkout(driver):

    login_page = LoginPage(driver)
    store_page = StorePage(driver)
    # Login
    login_page.open()
    login_page.login(
        ConfigTest.VALID_USERNAME,
        ConfigTest.VALID_PASSWORD
    )
    # Verifying login success
    assert login_page.is_logged_in()

    # Adding item to cart
    store_page.add_item_to_cart()

    # Opening shopping cart
    store_page.open_shopping_cart()

    assert store_page.is_in_cart()

    # Complete purchase
    store_page.checkout(
        ConfigTest.FIRST_NAME,
        ConfigTest.LAST_NAME,
        ConfigTest.POSTAL_CODE
    )
    store_page.finish_order()

    # Verifying order finalization
    assert store_page.is_finished()