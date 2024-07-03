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
    .key_up(Keys.SHIFT)\
    .send_keys('def')\
    .key_down(Keys.SHIFT)\
    .send_keys('ghi')\
    .perform()
time.sleep(5)
