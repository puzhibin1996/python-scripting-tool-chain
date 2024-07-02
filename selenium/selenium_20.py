from selenium import webdriver

driver = webdriver.Edge()

driver.get("https://music.163.com")
driver.add_cookie({'name': 'test1',"value":'cookie1'})
driver.add_cookie({'name': 'test2',"value":'cookie2'})

print(driver.get_cookie("test1"))
print(driver.get_cookie("test2"))
print(driver.get_cookies())