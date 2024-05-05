import time
from selenium import webdriver
from filters.choose_filters import Choose_filters
from pages.cart_page import Cart_page
from pages.second_shop_page import Second_shop_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.product_page import Product_page


def test_select_product():
    driver = webdriver.Chrome()

    print("Start Test")

    login = Login_page(driver)
    login.autorisation()
    time.sleep(3)

    filters = Choose_filters(driver)
    filters.choose_filters()
    driver.execute_script("window.scrollTo(0, 800)")

    pp = Product_page(driver)
    pp.select_product()

    ssp = Second_shop_page(driver)
    ssp.open_second_shop()

    cp = Cart_page(driver)
    cp.product_confirmation()

    fp = Finish_page(driver)
    fp.finish()
    time.sleep(10)





