import time
import pytest

from main_page import MainPage
from base_page import BasePage
from basket_page import BasketPage
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

link = "http://media.test.itass.local/customers"

# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     # return browser
#     yield browser
#     print("\nquit browser..")
#     browser.quit()


# class TestMainPage1():
# вызываем фикстуру в тесте, передав ее как параметр
# создание внутреннего клиента
@pytest.mark.parametrize('selector, value, selector1, value1, selector2, value2, selector3, value3',
                         [("#name", "test1@yandex.ru", "#email", "teывап2@yanывапdex.ru", "#phone1", "test3@yandex.ru", "#site", "test4@yandex.ru"),
                          ("#email", "teывап2@yanывапdex.ru", 79992244333, "teывап2@yanывапdex.r", 12345, "city", 2020202032, 222444882),
                          ("#phone1", "test3@yandex.ru", 79992244333, "test3@yandex.r", 12345, "city", 2020202023, 222444883),
                          ("#site", "test4@yandex.ru", 79992244333, "test4@yandex.r", 12345, "city", 2020202024, 222444884)])
def test_guest(browser, selector, value, selector1, value1, selector2, value2, selector3, value3):
    # browser.get(link)
    # time.sleep(2)
    # browser.find_element_by_id("details-button").click()
    # browser.find_element_by_id("proceed-link").click()
    # # driver.get("http://media.test.itass.local")
    # browser.find_element_by_id("userNameInput").send_keys("ext_kolzin_a")
    # time.sleep(1)
    # browser.find_element_by_id("passwordInput").send_keys("Overlor1")
    # browser.find_element_by_id("submitButton").click()

    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()

    time.sleep(2)
    input = browser.find_element_by_css_selector("#root > div > div > div > header > a > button")
    input.click()
    time.sleep(1)

    mass_selector = [selector, selector1, selector2, selector3]
    mass_value = [value, value1, value2, value3]

    # input = browser.find_element(By.XPATH, "// *[ @ id = 'root'] / div / div[3] / form / article[1] / section / div / div[1] / label / div / div")
    # input.click()


    input = browser.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[3]/form/div[1]/span[2]")
    status = input.text
    assert status == "Анкета не отправлена"

    # переключение на внутреннего клиента
    input = browser.find_element_by_css_selector(
        "#root > div > div > div > div.MDTTD808z7GuhtYhNCiyx > form > section:nth-child(3) > section > div > div._2z02StXLta1l1pMy9RZjqn._2KqIDt_bTCe7sb8_y5pdt0._3vXHzL1qtcips0rxKwEhuQ > label > div")
    input.click()

    i = 0
    for ii in mass_selector:

        # поля
        input = browser.find_element_by_css_selector(mass_selector[i])
        input.send_keys(mass_value[i])

        # клик по кнопке сохранить
        browser.find_element_by_css_selector(
            "#root > div > div > div > div.MDTTD808z7GuhtYhNCiyx > form > div.IKVnscL2xZb4_HAppSRik > div > div > button._1JPTNwXTDV_vLByphy1l-O.M9c1UcWhIvzGEP-ZtlSLa._2bMXaBwkLZj8rpG7EdgcRt").click()
        time.sleep(2)
        browser.execute_script('window.scrollTo(0,0);')

        # проверка на наличие надписи "Некорректное значение"
        input1 = browser.find_element_by_class_name("_2BdPeWfKXp-TXCYIUAZiad")
        status1 = input1.text
        assert status1 == "Некорректное значение"
        time.sleep(3)

        # преписка к значению в поле(изменение поля)
        input = browser.find_element_by_css_selector(mass_selector[i])
        input.send_keys("f")

        base_page = BasePage(browser, browser.current_url)
        assert base_page.is_element_present(By.CLASS_NAME, "_2BdPeWfKXp-TXCYIUAZiad")

        base_page = BasePage(browser, browser.current_url)
        assert base_page.is_element_present(By.LINK_TEXT, "Некорректное значение") == False

        input = browser.find_element_by_css_selector(mass_selector[i])
        input.clear()
        i = i + 1


    # basket_page = BasketPage(browser, browser.current_url)
    # basket_page.is_basket_empty()
    #
    # # проверка на наличие элемента на странице
    # red = True
    # try:
    #     browser.find_element_by_class_name("_2BdPeWfKXp-TXCYIUAZiad")
    # except NoSuchElementException:
    #     red = False
    # assert red == True
    #
    # red = True
    # try:
    #     browser.find_element_by_link_text("Некорректное значение")
    # except NoSuchElementException:
    #     red = False
    # assert red == False
    # time.sleep(3)

