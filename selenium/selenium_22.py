from selenium import webdriver

driver = webdriver.Edge()

driver.get("https://music.163.com")

driver.add_cookie({"name": "foo", "value": "value", 'sameSite': 'Strict'})
driver.add_cookie({"name": "foo1", "value": "value", 'sameSite': 'Lax'})

cookie1 = driver.get_cookie("foo")
cookie2 = driver.get_cookie("foo1")
print(cookie1)
print(cookie2)
