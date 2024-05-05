from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Finish_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    finish_order_button = "//*[@id='__layout']/div/div[4]/aside[7]/div[2]/div/div[1]/div/div/div/div/article/div/section/section/footer/button"
    continue_as_guest_button = "//button[@class='C9vd1 _5u8pb ce6pA yT+YV Q7ChL eYY+b']"
    final_price_in_cart = "//div[@class='price-animated']"
    #Getters

    def get_finish_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_order_button)))

    def get_continue_as_guest_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_as_guest_button)))

    def get_final_price_in_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.final_price_in_cart)))


    #Actions
    def click_finish_order_button(self):            # Move to the conformation order page
        self.get_finish_order_button().click()
        print("Click finish order button")

    def click_continue_as_guest_button(self):       # Continue as a guest (no need to login in the second site)
        self.get_continue_as_guest_button().click()
        print("Click continue as guest button")


    #Methods

    def finish(self):
        self.get_current_url()
        self.click_finish_order_button()
        self.click_continue_as_guest_button()
        self.assert_price(self.get_final_price_in_cart(), '1850')
        self.get_screenshot()


