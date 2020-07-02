import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#link = "http://suninjuly.github.io/find_link_text_redirect13.html"
link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input = browser.find_element_by_css_selector("body > div > form > div.first_block > div.form-group.third_class > input")
    input.send_keys("rggfghfg@yandex.ru")
    input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[1]/input")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.second_block > div.form-group.second_class > input")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(8)
    browser.quit()