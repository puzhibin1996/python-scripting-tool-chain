from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.set_window_size(400,500)
driver.get("https://selenium.dev/selenium/web/scrolling_tests/frame_with_nested_scrolling_frame_out_of_view.html")

footer = driver.find_element(By.TAG_NAME,"footer")
scroll_origin = ScrollOrigin.from_element(footer,0,-50)

ActionChains(driver)\
    .scroll_from_origin(scroll_origin,0,200)\
    .perform()


sleep(2)
