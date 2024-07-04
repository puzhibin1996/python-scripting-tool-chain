import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.set_window_size(400,500)
driver.get("https://selenium.dev/selenium/web/scrolling_tests/frame_with_nested_scrolling_frame_out_of_view.html")

footer = driver.find_element(By.TAG_NAME,'footer')
delta_y = footer.rect['y']

ActionChains(driver)\
    .scroll_by_amount(0, delta_y)\
    .perform()

time.sleep(2)
