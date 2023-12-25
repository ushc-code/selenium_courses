from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

import funcLog


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    price= WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element(By.ID,"book").click()

    x = browser.find_element(By.ID, "input_value")
    result = funcLog.calc(x.text)
    browser.find_element(By.ID, "answer").send_keys(result)
    browser.find_element(By.ID, "solve").click()
finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()