from selenium import webdriver

driver = webdriver.Edge()
driver.get("https://www.baidu.com")

driver.add_cookie({"name":"foo","value":"bar"})

print(driver.get_cookie("foo"))
