import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get("https://www.google.com")

driver.find_element(By.CSS_SELECTOR, "[name='wd']").send_keys("webElement")

attr = driver.switch_to.active_element.get_attribute("title")
print(attr)

time.sleep(5)