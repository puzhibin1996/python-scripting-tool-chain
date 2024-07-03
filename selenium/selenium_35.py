import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.set_window_size(400,600)
driver.get('https://selenium.dev/selenium/web/single_text_input.html')
text_input = driver.find_element(By.ID,"textInput")
ActionChains(driver)\
    .send_keys_to_element(text_input,'abc')\
    .perform()

time.sleep(4)