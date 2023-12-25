from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "num1").text
    y= browser.find_element(By.ID, "num2").text
    result = int(x)+int(y)

    print(result)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(result)) # ищем элемент с текстом "Python"
    browser.find_element(By.CLASS_NAME, "btn").click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()