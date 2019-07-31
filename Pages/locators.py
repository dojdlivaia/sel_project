from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTOR_FORM = (By.CSS_SELECTOR, "#register_form")
class ProductPageLocators(object):
    ADD_TO_BASCKET = (By.CLASS_NAME, "btn-add-to-basket")
    PRICE = (By.CLASS_NAME, "price_color")
    BOOK_NAME = (By.CSS_SELECTOR, "div.prduct_main h1")
