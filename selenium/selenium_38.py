from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get('https://selenium.dev/selenium/web/mouse_interaction.html')
driver.find_element(By.ID, "click").click()
action = ActionChains(driver)
action.pointer_action.pointer_down(MouseButton.BACK)
action.pointer_action.pointer_up(MouseButton.BACK)
action.perform()
