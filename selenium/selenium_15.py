import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()
driver.get("https://www.selenium.dev/selenium/web/inputs.html")
is_email_visible = driver.find_element(By.NAME,"button_input").is_enabled()
print(is_email_visible)
time.sleep(5)
