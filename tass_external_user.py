import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://media.test.itass.local/customers"


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
    # создание внутреннего клиента
    @pytest.mark.parametrize('name, email, phone, adres, id, city, inn, kpp',
                             [("ivan-", "test1@yandex.ru", 79992244333, "adres", 12345, "city", 2020202033,
                               222444881),
                              ("petr-", "test2@yandex.ru", 79992244333, "adres", 12345, "city", 2020202032,
                               222444882),
                              ("sony-", "test3@yandex.ru", 79992244333, "adres", 12345, "city", 2020202023,
                               222444883),
                              (
                                      "dcc-", "test4@yandex.ru", 79992244333, "adres", 12345, "city", 2020202024,
                                      222444884)])
    def test_guest(self, browser, name, email, phone, adres, id, city, inn, kpp):
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
        # input = browser.find_element(By.XPATH, "// *[ @ id = 'root'] / div / div[3] / form / article[1] / section / div / div[1] / label / div / div")
        # input.click()
        input = browser.find_element(By.XPATH, "//*[@id='root']/div/div/div[3]/form/div[1]/span[2]")
        status = input.text
        assert status == "Анкета не отправлена"

        input = browser.find_element_by_css_selector(
            "#root > div > div > div.MDTTD808z7GuhtYhNCiyx > form > section:nth-child(3) > section > div > div._2z02StXLta1l1pMy9RZjqn._2KqIDt_bTCe7sb8_y5pdt0._3vXHzL1qtcips0rxKwEhuQ > label > div")
        input.click()

        # название
        input = browser.find_element_by_id("name")
        input.send_keys(name)
        browser.execute_script('window.scrollTo(0,100);')

        # дата
        time.sleep(1)
        browser.find_element(By.XPATH,
                             "/html/body/div[1]/div/div/div[3]/form/section[1]/section/div/div[6]/div/div/div/div/input").send_keys(
            "11.09.2020")
        # input.send_keys("11.09.2020")
        input = browser.find_element(By.XPATH,
                                     "/html/body/div[1]/div/div/div[3]/form/section[1]/section/div/div[6]/div/div/div/div/input")
        input.click()
        input = browser.find_element_by_css_selector(
            "#modal-root > div > div > div.Z36NgfhhAdPjQ8yA25RkK > div._2i6ikGcmypNEzZ5LByRFPh > div > div > div:nth-child(4) > div > div._1JOxArCwFF0kO-vBRkvC0j > div:nth-child(3) > div:nth-child(5)")
        input.click()

        # email
        input = browser.find_element(By.XPATH, "//*[@id='email']")
        input.send_keys(email)

        # телефон
        input = browser.find_element(By.XPATH, "//*[@id='phone1']")
        input.send_keys(phone)

        # сфера деятеьлности
        browser.find_element_by_css_selector(
            "#root > div > div > div.MDTTD808z7GuhtYhNCiyx > form > section:nth-child(1) > section > div > div:nth-child(7) > div > div > div > div > div > svg").click()
        time.sleep(0.5)
        browser.find_element_by_class_name("_2L3E4ziW_4O8Dr95BBr2YU").click()

        # менеджер
        input = browser.find_element_by_css_selector(
            "#root > div > div > div.MDTTD808z7GuhtYhNCiyx > form > section:nth-child(1) > section > div > div:nth-child(8) > div > div > div > div > div > p")
        input.click()
        # browser.find_element_by_css_selector("#root > div > div > div.MDTTD808z7GuhtYhNCiyx > form > section:nth-child(3) > section > div > div:nth-child(8) > div > div > div > div > div > p").send_keys("ал")
        input1 = browser.find_element_by_css_selector(
            "#root > div > div > div.MDTTD808z7GuhtYhNCiyx > form > section:nth-child(1) > section > div > div:nth-child(8) > div > div > div > div > div > div._3oZXeuXkvti9Sua7CKx_8d > div > div:nth-child(1) > div:nth-child(1) > div")
        time.sleep(0.5)
        input1.click()

        # валюта
        # input = browser.find_element_by_css_selector(
        #     "#root > div > div > div.MDTTD808z7GuhtYhNCiyx > form > section:nth-child(3) > section > div > div:nth-child(10) > div > div > div > div > div > p")
        # input.click()
        # input1 = browser.find_element_by_css_selector(
        #     "#root > div > div > div.MDTTD808z7GuhtYhNCiyx > form > section:nth-child(3) > section > div > div:nth-child(10) > div > div > div > div > div > div._3oZXeuXkvti9Sua7CKx_8d > div > div:nth-child(1) > div:nth-child(1) > div")
        # input1.click()

        # страна
        input = browser.find_element(By.XPATH,
                                     "//*[@id='root']/div/div/div[3]/form/section[1]/section/div/div[9]/div/div/div/div/div/p")
        input.click()
        input1 = browser.find_element(By.XPATH,
                                      "//*[@id='root']/div/div/div[3]/form/section[1]/section/div/div[9]/div/div/div/div/div/div[3]/div/div[1]/div[2]/div")
        time.sleep(1)
        input1.click()

        # источник
        # input = browser.find_element_by_css_selector(
        #     "#root > div > div > div.MDTTD808z7GuhtYhNCiyx > form > section:nth-child(3) > section > div > div:nth-child(11) > div > div > div > div > div > p")
        # input.click()
        # time.sleep(0.5)
        # input1 = browser.find_element_by_css_selector(
        #     "#root > div > div > div.MDTTD808z7GuhtYhNCiyx > form > section:nth-child(3) > section > div > div:nth-child(11) > div > div > div > div > div > div._3oZXeuXkvti9Sua7CKx_8d > div > div:nth-child(1) > div:nth-child(3) > div")
        # input1.click()

        input = browser.find_element_by_css_selector("#mainAddress\.addressTitle")
        input.send_keys(adres)

        input = browser.find_element_by_css_selector("#mainAddress\.postCode")
        input.send_keys(id)

        input = browser.find_element_by_css_selector("#mainAddress\.city")
        input.send_keys(city)

        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # input = browser.find_element_by_id("inn")
        # input.send_keys(inn)
        #
        # input = browser.find_element_by_css_id("kpp")
        # input.send_keys(kpp)

        input1 = browser.find_element_by_css_selector(
            "#isMatchesWithPrimaryAddress")
        input1.click()

        # страна
        input = browser.find_element_by_css_selector(
            "#root > div > div > div.MDTTD808z7GuhtYhNCiyx > form > section:nth-child(2) > section > div._27thvWYvYYIFOWBO-Vt4uD._2zsxRxG1WzmnuxkzvdH11K > div > div > div > div > div > div > div.neLGgSRt5uRIuiNDvGsFB.bmHzo9bsOwH0VJrddnfGj")
        input.click()
        input1 = browser.find_element_by_css_selector(
            "#root > div > div > div.MDTTD808z7GuhtYhNCiyx > form > section:nth-child(2) > section > div._27thvWYvYYIFOWBO-Vt4uD._2zsxRxG1WzmnuxkzvdH11K > div > div > div > div > div > div > div._3oZXeuXkvti9Sua7CKx_8d > div > div:nth-child(1) > div:nth-child(3) > div")
        time.sleep(1)
        input1.click()

        browser.find_element_by_css_selector(
            "#root > div > div > div.MDTTD808z7GuhtYhNCiyx > form > div.IKVnscL2xZb4_HAppSRik > div > div > button._1JPTNwXTDV_vLByphy1l-O.M9c1UcWhIvzGEP-ZtlSLa._2bMXaBwkLZj8rpG7EdgcRt").click()
        time.sleep(1)
        browser.execute_script('window.scrollTo(0,0);')
        # time.sleep(1)

        input1 = browser.find_element_by_id("modal-root")
        status1 = input1.text
        assert status1 == "Клиент создан"
        time.sleep(2)

        # input1 = browser.find_element_by_css_selector(
        #     "#root > div > div > div.MDTTD808z7GuhtYhNCiyx > div._3FtI9K_rYuNqNUawu1Ow7K._2dqkqLWSBZAvRV2i3XPaE1 > header > button")
        # status1 = input1.text
        # assert status1 == "Новый продукт"
        # time.sleep(2)

        # input1 = browser.find_element_by_id("modal-root")
        # status1 = input1.text
        # assert status1 == "Клиент с такими данными уже существует."
        # time.sleep(2)




