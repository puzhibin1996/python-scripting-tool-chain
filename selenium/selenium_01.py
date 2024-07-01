import time

from selenium import webdriver

browser = webdriver.Edge()
browser.get('https://www.baidu.com')

print('当前页面标题是：', browser.title)
assert '百度一下，你就知道' in browser.title

elem=browser.find_element('id','kw')
elem.send_keys('selenium')
a1=browser.find_element('id','su')
a1.click()
time.sleep(2)
