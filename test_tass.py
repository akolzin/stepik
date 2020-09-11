import time
import pytest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

link = "http://media.test.itass.local/customers"

red = ""

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    # return browser
    yield browser
    print("\nquit browser..")
    browser.quit()

def check_exists(xpath):
    try:
        browser.find_element_by_class_name(xpath)
    except NoSuchElementException:
        red = False
    red = True

def check_exists1(xpath):
    try:
        browser.find_element_by_link_text(xpath)
    except NoSuchElementException:
        red = True
    red = False


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    # создание внутреннего клиента
    @pytest.mark.parametrize('selector, value, phone, value1, id, city, inn, kpp',
                             [("#name", "test1@yandex.ru", 79992244333, "test1@yandex.r", 12345, "city", 2020202033,
                               222444881),
                              ("#email", "teывап2@yanывапdex.ru", 79992244333, "teывап2@yanывапdex.r", 12345, "city", 2020202032,
                               222444882),
                              ("#phone1", "test3@yandex.ru", 79992244333, "test3@yandex.r", 12345, "city", 2020202023,
                               222444883),
                              (
                                      "#site", "test4@yandex.ru", 79992244333, "test4@yandex.r", 12345, "city", 2020202024,
                                      222444884)])
    def test_guest(self, browser, selector, value, phone, value1, id, city, inn, kpp):
        browser.get(link)
        time.sleep(2)
        browser.find_element_by_id("details-button").click()
        browser.find_element_by_id("proceed-link").click()
        # driver.get("http://media.test.itass.local")
        browser.find_element_by_id("userNameInput").send_keys("ext_kolzin_a")
        time.sleep(1)
        browser.find_element_by_id("passwordInput").send_keys("Overlor1")
        browser.find_element_by_id("submitButton").click()
        time.sleep(2)
        input = browser.find_element_by_css_selector("#root > div > div > div > header > a > button")
        input.click()
        time.sleep(1)

        # input = browser.find_element(By.XPATH, "// *[ @ id = 'root'] / div / div[3] / form / article[1] / section / div / div[1] / label / div / div")
        # input.click()
        input = browser.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[3]/form/div[1]/span[2]")
        status = input.text
        assert status == "Анкета не отправлена"

        input = browser.find_element_by_css_selector(
            "#root > div > div > div > div.MDTTD808z7GuhtYhNCiyx > form > section:nth-child(3) > section > div > div._2z02StXLta1l1pMy9RZjqn._2KqIDt_bTCe7sb8_y5pdt0._3vXHzL1qtcips0rxKwEhuQ > label > div")
        input.click()

        # поля
        input = browser.find_element_by_css_selector(selector)
        input.send_keys(value)

        browser.find_element_by_css_selector(
            "#root > div > div > div > div.MDTTD808z7GuhtYhNCiyx > form > div.IKVnscL2xZb4_HAppSRik > div > div > button._1JPTNwXTDV_vLByphy1l-O.M9c1UcWhIvzGEP-ZtlSLa._2bMXaBwkLZj8rpG7EdgcRt").click()
        time.sleep(2)
        browser.execute_script('window.scrollTo(0,0);')

        input1 = browser.find_element_by_class_name("_2BdPeWfKXp-TXCYIUAZiad")
        status1 = input1.text
        assert status1 == "Некорректное значение"
        time.sleep(3)

        # поля
        input = browser.find_element_by_css_selector(selector)
        input.send_keys("f")

        red = True

        try:
            browser.find_element_by_class_name("_2BdPeWfKXp-TXCYIUAZiad")
        except NoSuchElementException:
            red = False


        # check_exists('_2BdPeWfKXp-TXCYIUAZiad')
        assert red == True

        red = True

        try:
            browser.find_element_by_link_text("Некорректное значение")
        except NoSuchElementException:
            red = False

        # check_exists("Некорректное значение")
        assert red == False


        # assert browser.find_element_by_class_name("_2BdPeWfKXp-TXCYIUAZiad")
        # status1 = input1.text
        # assert browser.find_element_by_link_text("Некорректное значение")
        time.sleep(3)

