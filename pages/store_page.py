from pages.base_page import BasePage
from locators import LocatorsStorePage

class StorePage(BasePage):
    
    def app_logo_is_visible(self):
        # Verify login success
        app_logo =  self.wait_for_presence(LocatorsStorePage.APP_LOGO)
        return app_logo.is_displayed()

    def open_sidebar(self):
        # Finding sidebar menu button
        sider_bar = self.wait_for_clickable(LocatorsStorePage.BURGER_SIDEBAR)
        # Clicking menu button
        sider_bar.click()

    def logout(self):
        #Finding logout button
        logout_button = self.wait_for_clickable(LocatorsStorePage.LOGOUT_BUTTON)
        #Logging out
        logout_button.click()

    def add_item_to_cart(self):
        # Finding the add backpack to cart button element
        add_backpack_button = self.wait_for_clickable(LocatorsStorePage.BACKPACK_BUTTON)
        # Adding the item into the cart
        add_backpack_button.click()

    def open_shopping_cart(self):
        # Finding the shopping cart button element
        shop_cart_button = self.wait_for_clickable(LocatorsStorePage.CART_BUTTON)
        # Going into the shopping cart
        shop_cart_button.click()

    def is_in_cart(self):
        # Verify item is in cart
        cart_title = self.wait_for_presence(LocatorsStorePage.CART_TITLE)
        item_name = self.wait_for_presence(LocatorsStorePage.ITEM_NAME)
        return cart_title.is_displayed() and item_name.is_displayed() 
    
    def checkout(self, first_name, last_name, postal_code):
        # Finding the checkout button element
        checkout_button = self.wait_for_clickable(LocatorsStorePage.CHECKOUT_BUTTON)
        # Checkout
        checkout_button.click()
        # Finding the first name field element
        first_name_field = self.wait_for_presence(LocatorsStorePage.FIRST_NAME)
        # Finding the last name field element
        last_name_field = self.wait_for_presence(LocatorsStorePage.LAST_NAME)
        # Finding the zip code field element
        postal_code_field = self.wait_for_presence(LocatorsStorePage.POSTAL_CODE)
        # Filling personal information
        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)
        postal_code_field.send_keys(postal_code)
        #Finding continue button element
        continue_button = self.wait_for_clickable(LocatorsStorePage.CONTINUE_BUTTON)
        # Submiting information
        continue_button.click()

    def finish_order(self):
        # Finding finish button element
        finish_button = self.wait_for_clickable(LocatorsStorePage.FINNISH_BUTTON)
        # Finilizing order
        finish_button.click()

    def is_finished(self):
        # Verify order finalization
        header_complete = self.wait_for_presence(LocatorsStorePage.HEADER_COMPLETE)
        return header_complete.is_displayed()