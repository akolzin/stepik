import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#link = "http://suninjuly.github.io/find_link_text_redirect13.html"
#link = "http://suninjuly.github.io/math.html"
link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath("//*[@id='num1']")
    x_element1 = browser.find_element_by_xpath("//*[@id='num2']")
    #print(x_element1)
    x = x_element.text
    x1 = x_element1.text
    #y = calc(x)
    y1 = int(x) + int(x1)
    print(x)
    print(x1)
    print(y1)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(y1))  # ищем элемент с текстом "Python"

    # input = browser.find_element_by_css_selector("#answer")
    # input.send_keys(y)
    # input1 = browser.find_element(By.XPATH, "//*[@id='robotCheckbox']")
    # input1.click()
    # input2 = browser.find_element(By.XPATH, "//*[@id='robotsRule']")
    # input2.click()

    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(8)
    browser.quit()