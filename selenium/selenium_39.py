import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.set_window_size(400,500)
driver.get("https://selenium.dev/selenium/web/scrolling_tests/frame_with_nested_scrolling_frame_out_of_view.html")

iframe = driver.find_element(By.TAG_NAME,'iframe')
ActionChains(driver)\
    .scroll_to_element(iframe)\
    .perform()

time.sleep(2)
