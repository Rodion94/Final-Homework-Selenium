import datetime

class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method Get current URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current URL " + get_url)


    """Methods assert word and price"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    def assert_price(self, price, result):
        value_price = price.text.replace(" ", '')
        number_value_price = float(value_price[0:4])
        assert number_value_price == float(result)
        print("Good value price")

    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot_' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\79617\\PycharmProjects\\final_homework\\screen\\' + name_screenshot)

