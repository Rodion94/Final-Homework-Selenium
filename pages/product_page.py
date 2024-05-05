from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Product_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    info_about_product_1 = "//a[@title='Кремовый пигмент Concrete Beige жидкие тени для век, подводка, помада, 4.5 мл']"
    title_product_1 = "//h1[@class='ty-product-block-title']"


    #Getters

    def get_info_about_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.info_about_product_1)))

    def get_title_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.title_product_1)))


    #Actions

    def click_info_about_product_1(self):
        self.get_info_about_product_1().click()
        print("Click more info about product 1")



    #Methods
    def select_product(self):
        self.get_current_url()
        self.assert_word(self.get_info_about_product_1(), "Кремовый пигмент Concrete Beige жидкие тени для век, подводка, помада, 4.5 мл")
        self.click_info_about_product_1()
        self.assert_word(self.get_title_product_1(), "Кремовый пигмент Concrete Beige жидкие тени для век, подводка, помада, 4.5 мл")



