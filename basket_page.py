from base_page import BasePage
from selenium.webdriver.common.by import By

class BasketPage(BasePage):

    def is_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE)


class BasketPageLocators():
    BASKET_MESSAGE = (By.CLASS_NAME, "_2BdPeWfKXp-TXCYIUAZiad")