from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.baidu.com/")
driver.find_element(By.TAG_NAME,'button').click()