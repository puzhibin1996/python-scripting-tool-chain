from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get("https://www.baidu.com/")

elements = driver.find_elements(By.TAG_NAME, 'a')

for element in elements:
    print(element.text)
