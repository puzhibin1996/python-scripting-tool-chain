import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

driver.find_element(By.NAME,"email_input").clear()

driver.find_element(By.NAME,"email_input").send_keys("1234@gmail.com")

time.sleep(4)