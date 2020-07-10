import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', ["https://stepik.org/lesson/236895/step/1",
                                      "https://stepik.org/lesson/236896/step/1",
                                      "https://stepik.org/lesson/236897/step/1",
                                      "https://stepik.org/lesson/236898/step/1",
                                      "https://stepik.org/lesson/236899/step/1",
                                      "https://stepik.org/lesson/236903/step/1",
                                      "https://stepik.org/lesson/236904/step/1",
                                      "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, language):
    #link = f"{language}"
    link = language
    browser.get(link)
    #browser.find_element_by_css_selector("#login_link")
    time.sleep(11)
    #input3 = browser.find_element_by_class_name("textarea string-quiz__textarea ember-text-area ember-view")
    input3 = browser.find_element_by_tag_name("textarea")
    # input3.click()
    # time.sleep(2)
    answer = math.log(int(time.time()))
    input3.send_keys(str(answer))
    # time.sleep(2)
    input1 = browser.find_element_by_xpath("//section/div/div[2]/div[4]/button")
    input1.click()
    time.sleep(2)
    input2 = browser.find_element_by_xpath("//section/div/div[1]/div/pre")
    x = input2.text
    assert x == "Correct!", "FATTAAALL"