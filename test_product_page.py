from pages.product_page import PageObject
import pytest
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]

 

@pytest.mark.parametrize('link', urls)  
def test_guest_can_add_product_to_cart(browser,link):
    page = PageObject(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.product_added()
    page.price_equal_basket()
