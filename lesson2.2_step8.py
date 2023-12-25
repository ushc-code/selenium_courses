from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstName = browser.find_element(By.NAME, "firstname")
    lastName = browser.find_element(By.NAME, "lastname")
    email = browser.find_element(By.NAME, "email")
    firstName.send_keys("Имя")
    lastName.send_keys("Фамилия")
    email.send_keys("Почта")

    current_dir = os.path.abspath(os.path.dirname(""))    # получаем путь к директории текущего исполняемого файла
    print(current_dir)
    file_path = os.path.join(current_dir, 'img.jpg')
    browser.find_element(By.ID, "file").send_keys(file_path)
    browser.find_element(By.CLASS_NAME, "btn").click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()