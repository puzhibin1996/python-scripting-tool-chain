import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

driver.find_element(By.NAME,"color_input").click()

time.sleep(5)