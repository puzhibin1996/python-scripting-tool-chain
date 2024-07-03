import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.baidu.com/")
input = driver.find_element(By.ID,"kw")
ActionChains(driver)\
    .move_to_element(input)\
    .pause(1)\
    .click_and_hold()\
    .pause(1)\
    .send_keys("selenium")\
    .pause(1)\
    .perform()

ActionBuilder(driver).clear_actions()
time.sleep(3)