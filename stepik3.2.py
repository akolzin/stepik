import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"

        try:
            browser = webdriver.Chrome()
            browser.get(link)

            input = browser.find_element_by_css_selector(
                "body > div > form > div.first_block > div.form-group.third_class > input")
            input.send_keys("rggfghfg@yandex.ru")
            input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.second_class > input")
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[1]/input")
            input3.send_keys("Smolensk")
            input4 = browser.find_element(By.CSS_SELECTOR,
                                          "body > div > form > div.second_block > div.form-group.second_class > input")
            input4.send_keys("Russia")
            time.sleep(3)
            button = browser.find_element(By.XPATH, "/html/body/div/form/button")
            button.click()

        finally:
            # закрываем браузер после всех манипуляций
            # time.sleep(8)
            browser.quit()

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"

        try:
            browser = webdriver.Chrome()
            browser.get(link)

            input = browser.find_element_by_css_selector(
                "body > div > form > div.first_block > div.form-group.third_class > input")
            input.send_keys("rggfghfg@yandex.ru")
            input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.second_class > input")
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[1]/input")
            input3.send_keys("Smolensk")
            input4 = browser.find_element(By.CSS_SELECTOR,
                                          "body > div > form > div.second_block > div.form-group.second_class > input")
            input4.send_keys("Russia")
            time.sleep(3)
            button = browser.find_element(By.XPATH, "/html/body/div/form/button")
            button.click()

        finally:
            # закрываем браузер после всех манипуляций
            # time.sleep(8)
            browser.quit()


if __name__ == "__main__":
    unittest.main()