from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base



class Second_shop_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.switch_to = None
        self.driver = driver


    #Locators

    open_second_shop_button = "//a[@href='https://goldapple.ru/14272300017-concrete']"
    main_word = "//a[@class='_9Bnes wEteb h92Dk uEBTc']"
    price = "//div[@class='_0OnLg +Ns2G']"

    #Getters

    def get_open_second_shop_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.open_second_shop_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price)))





    #Actions

    def click_open_second_shop_button(self):
        self.get_open_second_shop_button().click()
        print("Click open second shop button")


    #Methods
    def open_second_shop(self):
        self.get_current_url()
        self.click_open_second_shop_button()
        windows_2 = self.driver.window_handles[1]
        self.driver.switch_to.window(windows_2)
        self.get_current_url()
        self.get_main_word()
        self.assert_word(self.get_main_word(), "KRYGINA COSMETICS")
        self.assert_price(self.get_price(), '1850')


