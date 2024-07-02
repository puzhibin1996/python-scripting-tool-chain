import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()
# driver.get("https://www.selenium.dev/selenium/web/inputs.html")
# driver.get("https://www.selenium.dev/selenium/web/colorPage.html")
driver.get("https://www.selenium.dev/selenium/web/linked_image.html")
# value= driver.find_element(By.NAME,"email_input").tag_name
# value = driver.find_element(By.NAME,"range_input").rect
# value = driver.find_element(By.ID,"namedColor").value_of_css_property('background-color')
value = driver.find_element(By.ID,"justanotherlink").text
# print(value)
time.sleep(5)
