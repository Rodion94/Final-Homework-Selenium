from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_page(Base):

    url = 'https://krygina.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators
    account_dropdown = "//a[@class='ty-account-info__title']"
    enter_button = "//a[@class='cm-dialog-opener cm-dialog-auto-size ty-btn ty-btn__primary']"
    email = "//input[@id='login_popup100']"
    password = "//input[@id='psw_popup100']"
    final_enter_button = "//button[@class='ty-btn__login ty-btn__secondary ty-btn']"



    #Getters

    def get_account_dropdown(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.account_dropdown)))
    def get_enter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_final_enter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.final_enter_button)))


    #Actions

    def click_account_dropdown(self):         # Close delivery information popup
        self.get_account_dropdown().click()
        print("Click account dropdown")
    def click_enter_button(self):
        self.get_enter_button().click()
        print("Click enter button")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input Email")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input Password")

    def click_final_enter_button(self):
        self.get_final_enter_button().click()
        print("Click enter button")


    #Methods
    def autorisation(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_account_dropdown()
        self.click_enter_button()
        self.input_email("test.mail07@yandex.ru")
        self.input_password("qwe123ZXC")
        self.click_final_enter_button()


