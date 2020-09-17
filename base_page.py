import math
import time

from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
# from .locators import BasePageLocators

link = "http://media.test.itass.local/customers"

class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
        self.browser.find_element_by_id("details-button").click()
        self.browser.find_element_by_id("proceed-link").click()
        # driver.get("http://media.test.itass.local")
        self.browser.find_element_by_id("userNameInput").send_keys("ext_kolzin_a")
        time.sleep(1)
        self.browser.find_element_by_id("passwordInput").send_keys("Overlor1")
        self.browser.find_element_by_id("submitButton").click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True