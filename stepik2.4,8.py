import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    element = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()

    x_element = browser.find_element_by_xpath("//*[@id='input_value']")
    #x_element1 = browser.find_element_by_xpath("//*[@id='num2']")
    #print(x_element1)
    x = x_element.text
    #x1 = x_element1.text
    y = calc(x)

    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)

    button = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(8)
    browser.quit()