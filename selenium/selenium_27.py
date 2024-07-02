from selenium import webdriver

driver = webdriver.Edge()
driver.get("https://www.baidu.com")
driver.save_screenshot('./screenshot.png')
driver.quit()