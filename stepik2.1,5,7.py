import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#link = "http://suninjuly.github.io/find_link_text_redirect13.html"
#link = "http://suninjuly.github.io/math.html"
link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath("//*[@id='treasure']")
    x_element1 = x_element.get_attribute("valuex")
    print(x_element1)
    #x = x_element1.text
    y = calc(x_element1)
    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)
    input1 = browser.find_element(By.XPATH, "//*[@id='robotCheckbox']")
    input1.click()
    input2 = browser.find_element(By.XPATH, "//*[@id='robotsRule']")
    input2.click()

    button = browser.find_element(By.XPATH, "/html/body/div/form/div/div/button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(8)
    browser.quit()