# from appium import webdriver
#
#
# desired_caps = {
#     'platformName': 'Android', # 被测手机是安卓
#     'platformVersion': '13', # 手机安卓版本
#     'deviceName': 'a2cec350', # 设备名，安卓手机可以随意填写
#     # 'automationName': 'UiAutomator2', # 指定使用 UiAutomator2
# }
#
# # 连接Appium Server，初始化自动化环境
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
from appium.webdriver import webdriver

# from appium_04 import webdriver

# Appium 服务器地址和端口
appium_server = 'http://localhost:4723/wd/hub'

# 应用相关配置
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '13',
    'deviceName': 'a2cec350',  # 设备名称，可以是真机或模拟器的设备名
    'appPackage': 'com.example.myapp',  # 应用的包名
    'appActivity': '.MainActivity',  # 应用的启动Activity
    'automationName': 'UiAutomator2',  # 使用UiAutomator2引擎，支持更多操作
}

# 连接到 Appium 服务器，创建 webdriver 对象
driver = webdriver.Remote(appium_server, desired_caps)

#
#
# import time
# from selenium import webdriver
#
# browser = webdriver.Edge()
# browser.get("http://www.baidu.com")
# time.sleep(10)