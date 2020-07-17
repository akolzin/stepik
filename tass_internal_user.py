import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://172.16.3.35:8088/customers"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    # return browser
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    @pytest.mark.parametrize('name, email, phone, adres, id, city, inn, kpp',
                             [("ivan", "test1@yandex.ru", 79992244333, "adres", 12345, "city", 2020202021, 222444881),
                              ("petr", "test2@yandex.ru", 79992244333, "adres", 12345, "city", 2020202022, 222444882),
                              ("sony", "test3@yandex.ru", 79992244333, "adres", 12345, "city", 2020202023, 222444883),
                              ("dc", "test4@yandex.ru", 79992244333, "adres", 12345, "city", 2020202024, 222444884)])
    def test_guest(self, browser, name, email, phone, adres, id, city, inn, kpp):
        browser.get(link)
        # input11 = browser.find_element_by_css_selector("#username")
        # input11.send_keys("admin1")
        # input12 = browser.find_element_by_css_selector("#password")
        # input12.send_keys("password")
        # input13 = browser.find_element_by_css_selector("#root > div > div.src-layouts-simple-simple-styles__content > div > form > button")
        # input13.click()
        time.sleep(2)
        input = browser.find_element_by_css_selector("#root > div > div > div > header > a > button")
        input.click()
        input = browser.find_element(By.XPATH, "// *[ @ id = 'root'] / div / div[3] / form / article[1] / section / div / div[1] / label / div / div")
        input.click()
        input = browser.find_element(By.XPATH, "// *[ @ id = 'root'] / div / div[3] / form / div[1] / span[2]")
        status = input.text
        assert status == "Анкета не отправлена"
        input = browser.find_element_by_css_selector("#name")
        input.send_keys(name)
        input = browser.find_element_by_css_selector("#root > div > div.src-components-tabs-tabs-styles__wrapper > form > article:nth-child(3) > section > div > div:nth-child(6) > div > div > div > div")
        input.click()
        input = browser.find_element_by_css_selector("#modal-root > div > div > div.src-components-calendar-body-body-styles__body > div.src-components-calendar-body-body-styles__scroll-container > div > div > div:nth-child(4) > div > div.src-components-calendar-month-month-styles__month-days > div:nth-child(3) > div:nth-child(5)")
        input.click()
        input = browser.find_element(By.XPATH, "//*[@id='email']")
        input.send_keys(email)

        input = browser.find_element_by_css_selector("#root > div > div.src-components-tabs-tabs-styles__wrapper > form > article:nth-child(3) > section > div > div:nth-child(5) > div > div > div > div > div")
        input.click()
        input = browser.find_element(By.XPATH,"//*[@id='root']/div/div[3]/form/article[1]/section/div/div[5]/div/div/div/div/div/div[2]/div/div[1]/div[1]")
        input.click()
        input = browser.find_element(By.XPATH, "//*[@id='phone1']")
        input.send_keys(phone)

        # сфера деятеьлности
        input = browser.find_element_by_css_selector("#root > div > div.src-components-tabs-tabs-styles__wrapper > form > article:nth-child(3) > section > div > div:nth-child(7) > div > div > div > div > div")
        input.click()
        input1 = browser.find_element_by_css_selector(
            "#root > div > div.src-components-tabs-tabs-styles__wrapper > form > article:nth-child(3) > section > div > div:nth-child(7) > div > div > div > div > div > div.src-components-select-select-styles__dropdown-container > div > div:nth-child(1) > div:nth-child(1) > div")
        input1.click()

        # менеджер
        input = browser.find_element_by_css_selector("#root > div > div.src-components-tabs-tabs-styles__wrapper > form > article:nth-child(3) > section > div > div:nth-child(8) > div > div > div > div > div")
        input.click()
        input1 = browser.find_element_by_css_selector(
            "#root > div > div.src-components-tabs-tabs-styles__wrapper > form > article:nth-child(3) > section > div > div:nth-child(8) > div > div > div > div > div > div.src-components-select-select-styles__dropdown-container > div > div:nth-child(1) > div:nth-child(2)")
        time.sleep(0.5)
        input1.click()

        # валюта
        # input = browser.find_element_by_css_selector("#root > div > div.src-components-tabs-tabs-styles__wrapper > form > article:nth-child(3) > section > div > div:nth-child(10) > div > div > div > div > div")
        # input.click()
        # input1 = browser.find_element_by_css_selector(
        #     "#root > div > div.src-components-tabs-tabs-styles__wrapper > form > article:nth-child(3) > section > div > div:nth-child(10) > div > div > div > div > div > div.src-components-select-select-styles__dropdown-container > div > div:nth-child(1) > div:nth-child(1) > div")
        # input1.click()

        # страна
        input = browser.find_element(By.XPATH, "//*[@id='root']/div/div[3]/form/article[1]/section/div/div[9]/div/div/div/div/div")
        input.click()
        input1 = browser.find_element(By.XPATH, "//*[@id='root']/div/div[3]/form/article[1]/section/div/div[9]/div/div/div/div/div/div[3]/div/div[1]/div[1]/div")
        input1.click()

        # источник
        # input = browser.find_element_by_css_selector("#root > div > div.src-components-tabs-tabs-styles__wrapper > form > article:nth-child(3) > section > div > div:nth-child(11) > div > div > div > div > div")
        # input.click()
        # time.sleep(0.5)
        # input1 = browser.find_element_by_css_selector(
        #     "#root > div > div.src-components-tabs-tabs-styles__wrapper > form > article:nth-child(3) > section > div > div:nth-child(11) > div > div > div > div > div > div.src-components-select-select-styles__dropdown-container > div > div:nth-child(1) > div:nth-child(3) > div")
        # input1.click()

        input = browser.find_element_by_css_selector("#mainAddress\.addressTitle")
        input.send_keys(adres)

        input = browser.find_element_by_css_selector("#mainAddress\.postCode")
        input.send_keys(id)

        input = browser.find_element_by_css_selector("#mainAddress\.city")
        input.send_keys(city)

        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # input = browser.find_element_by_css_selector("#inn")
        # input.send_keys(inn)
        #
        # input = browser.find_element_by_css_selector("#kpp")
        # input.send_keys(kpp)

        input1 = browser.find_element_by_css_selector(
            "#isMatchesWithPrimaryAddress")
        input1.click()

        # страна
        input = browser.find_element_by_css_selector(
            "#root > div > div.src-components-tabs-tabs-styles__wrapper > form > article:nth-child(4) > section > div.src-components-grid-grid-styles__container.src-components-grid-grid-styles__spacing-40px > div > div > div > div > div > div > svg.src-components-select-select-styles__arrow-icon-reversed.src-components-select-select-styles__arrow-icon")
        input.click()
        input1 = browser.find_element_by_css_selector(
            "#root > div > div.src-components-tabs-tabs-styles__wrapper > form > article:nth-child(4) > section > div.src-components-grid-grid-styles__container.src-components-grid-grid-styles__spacing-40px > div > div > div > div > div > div > div.src-components-select-select-styles__dropdown-container > div > div:nth-child(1) > div:nth-child(1) > div")
        input1.click()


