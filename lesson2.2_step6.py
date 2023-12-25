from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "input_value")
    result = calc(x.text)
    browser.find_element(By.ID, "answer").send_keys(result)
    browser.find_element(By.ID,"robotCheckbox").click()

    button = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    browser.find_element(By.CLASS_NAME, "btn").click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()