from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

""""Choose Filters block"""
class Choose_filters(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators
    catalog_button = "//div[@id='sw_dropdown_219']"
    more_button = "//a[@class='ty-menu__submenu-alt-link']"
    filter_dropdown = "//span[@class='ty-sidebox__title-toggle']"
    min_price = "//input[@id='slider_89_1_left']"
    max_price = "//input[@id='slider_89_1_right']"
    lipstick_filter = "//span[contains(text(), 'Помада')]"



    #Getters

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_more_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.more_button)))

    def get_filter_dropdown(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_dropdown)))

    def get_min_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.min_price)))

    def get_max_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.max_price)))

    def get_lipstick_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.lipstick_filter)))


    #Actions

    def click_catalog_button(self):         # Open Catalog
        self.get_catalog_button().click()
        print("Click catalog button")

    def click_more_button(self):          # Choose More option
        self.get_more_button().click()
        print("Click more button")

    def click_filter_dropdown(self):          # Open Filters dropdown
        self.get_filter_dropdown().click()
        print("Click filter dropdown")

    def get_input_min_price(self):
        self.get_min_price().click()
        print("Choose min price input")

    def clear_input_min_price(self):
        self.get_min_price().send_keys(Keys.CONTROL + "a")
        print("Clear min price input")

    def input_min_price(self):
        self.get_min_price().send_keys("1200")
        print("Add min price")

    def get_input_max_price(self):
        self.get_max_price().click()
        print("Choose max price input")

    def clear_input_max_price(self):
        self.get_max_price().send_keys(Keys.CONTROL + "a")
        print("Clear max price input")

    def input_max_price(self):
        self.get_max_price().send_keys("1900")
        print("Add max price")

    def click_lipstick_filter(self):     # Choose high rate filter
        self.get_lipstick_filter().click()
        print("Choose Lipstick filter")


    #Methods
    def choose_filters(self):
        self.get_current_url()
        self.click_catalog_button()
        self.click_more_button()
        self.click_filter_dropdown()
        self.get_input_min_price()
        self.clear_input_min_price()
        self.input_min_price()
        self.get_input_max_price()
        self.clear_input_max_price()
        self.input_max_price()
        self.click_lipstick_filter()


