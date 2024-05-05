from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Cart_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators
    add_to_cart_button = "//button[@class='C9vd1 _5u8pb dpASR yT+YV Q7ChL']"
    enter_cart_button = "//button[@class='C9vd1 wEteb h92Dk ga-header__tab ga-header__tab_type_cart ga-header__action']"
    final_price = "//*[@id='__layout']/div/div[4]/aside[7]/div[2]/div/div[1]/div/div/div/div/article/div/section/section/div[1]/div[2]/div/div[4]/dt[2]/div/div[1]/div"



    #Getters

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_enter_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_cart_button)))

    def get_final_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.final_price)))


    #Actions

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("Click add to cart button")

    def click_enter_cart_button(self):
        self.get_enter_cart_button().click()
        print("Click enter cart button")


    #Methods
    def product_confirmation(self):
        self.get_current_url()
        self.click_add_to_cart_button()
        self.click_enter_cart_button()
        self.assert_price(self.get_final_price(), '1850')


