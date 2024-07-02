from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.selenium.dev/selenium/web/inputs.html")
email_txt = driver.find_element(By.NAME,"email_input")
value_info = email_txt.get_attribute("value")
print(value_info)