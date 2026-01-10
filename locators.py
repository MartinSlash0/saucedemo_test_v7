from selenium.webdriver.common.by import By

# Locators of elements for each page in different classes

class LocatorsLogInPage():
    USER_NAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_PROMPT =(By.CSS_SELECTOR, "h3[data-test='error']")

class LocatorsStorePage():
    APP_LOGO = (By.CSS_SELECTOR, "div[class='app_logo']")
    BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BUTTON = (By.CSS_SELECTOR, "a[class='shopping_cart_link']")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINNISH_BUTTON = (By.ID, "finish")
    HEADER_COMPLETE = (By.CSS_SELECTOR, "h2[class='complete-header']")
    ITEM_NAME = (By.CSS_SELECTOR, "div[class='inventory_item_name']")
    CART_TITLE = (By.CSS_SELECTOR, "span[class='title']")