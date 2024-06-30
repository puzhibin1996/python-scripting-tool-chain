import time
import logging
from appium.webdriver import Remote

# Enable logging
logging.basicConfig(level=logging.DEBUG)

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '12',
    'deviceName': '127.0.0.1:62001',
    'appPackage': 'com.android.settings',
    'appActivity': 'com.android.settings.SubSettings'
}

driver = Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(5)
driver.quit()
