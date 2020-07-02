import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input = browser.find_element_by_css_selector("body > div > form > div > input:nth-child(2)")
    input.send_keys("Ivan")
    input1 = browser.find_element(By.XPATH, "/html/body/div/form/div/input[2]")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "/html/body/div/form/div/input[3]")
    input2.send_keys("rggfghfg@yandex.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element = browser.find_element(By.XPATH, "//*[@id='file']")
    element.send_keys(file_path)
    print(os.path.abspath(__file__))

    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(8)
    browser.quit()