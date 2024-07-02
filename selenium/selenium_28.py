from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.example.com")
ele = driver.find_element(By.CSS_SELECTOR, "h1")
# ele.screenshot('./h1_screenshot.png')
driver.execute_script('return arguments[0].innerText')
driver.quit()