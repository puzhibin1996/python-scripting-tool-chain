import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.set_window_size(400,600)
driver.get('https://selenium.dev/selenium/web/single_text_input.html')
ActionChains(driver)\
    .key_down(Keys.SHIFT)\
    .send_keys('abc')\
    .perform()
assert driver.find_element(By.ID,"textInput").get_attribute("value") == "ABC"
time.sleep(5)
