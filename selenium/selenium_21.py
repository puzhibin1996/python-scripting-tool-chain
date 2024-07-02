from selenium import webdriver

driver = webdriver.Edge()
driver.get("https://www.baidu.com/")
driver.add_cookie({'name': 'test1', 'value': 'cookie1'})
driver.add_cookie({'name': 'test2', 'value': 'cookie2'})

print(driver.get_cookies())
driver.delete_all_cookies()
print("删除所有cookie了")
print(driver.get_cookies())
