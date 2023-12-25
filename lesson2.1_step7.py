from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "treasure").get_attribute("valuex");
    result = calc(x)
    browser.find_element(By.ID, "answer").send_keys(result)

    browser.find_element(By.ID,"robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CLASS_NAME, "btn").click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()