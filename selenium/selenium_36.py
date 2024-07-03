import sys
import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.set_window_size(300,500)
driver.get('https://selenium.dev/selenium/web/single_text_input.html')
cmd_ctrl = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL

ActionChains(driver) \
    .send_keys("Selenium!") \
    .send_keys(Keys.ARROW_LEFT) \
    .key_down(Keys.SHIFT) \
    .send_keys(Keys.ARROW_UP) \
    .key_up(Keys.SHIFT) \
    .key_down(cmd_ctrl) \
    .send_keys("xvv") \
    .key_up(cmd_ctrl) \
    .perform()

# assert driver.find_element(By.ID, "textInput").get_attribute('value') == "SeleniumSelenium!"

time.sleep(5)