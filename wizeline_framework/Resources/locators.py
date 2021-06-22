from selenium.webdriver.common.by import By


class LoginPageElements:
    LOGIN_BTN = (By.ID, "login-button")
    PASS_BOX = (By.ID, "password")
    USR_BOX = (By.ID, "user-name")
    ERROR_LOGIN_MSG = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[3]/h3[1]")


class HomePageElements:
    PROD_LABEL = (By.CLASS_NAME, "title")
    BAR_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_BTN = (By.ID, "logout_sidebar_link")
    DROP_BAR = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/span[1]/select[1]")
    SORT_PRICE_LH = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/span[1]/select[1]/option[3]")
    PRICES = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BTN = (By.TAG_NAME, "button")
    CART_BTN = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]")
    ADD_CART_BTN_ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")


class CartPageElements:
    IN_CART_ELEMENTS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BTN = (By.ID, "checkout")


class CheckStepOnePageElements:
    NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")


class CheckStepTwoPageElements:
    FINISH_BTN = (By.ID, "finish")
    OVERVIEW_LABEL = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]")


class CheckoutCompleteElements:
    COMPLETE_LABEL = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]")
