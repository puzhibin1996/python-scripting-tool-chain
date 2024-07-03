import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.set_window_size(500,600)
driver.get('https://selenium.dev/selenium/web/mouse_interaction.html')

clickable = driver.find_element(By.ID,"clickable")
ActionChains(driver)\
    .context_click(clickable)\
    .perform()

time.sleep(3)