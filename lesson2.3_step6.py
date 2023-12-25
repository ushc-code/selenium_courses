from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CLASS_NAME, "trollface").click()
    window_name = browser.window_handles[1]
    browser.switch_to.window(window_name)
    x = browser.find_element(By.ID, "input_value")
    result = calc(x.text)
    browser.find_element(By.ID, "answer").send_keys(result)
    browser.find_element(By.CLASS_NAME, "btn").click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()