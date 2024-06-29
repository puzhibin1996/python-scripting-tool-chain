
import time
import logging
from appium.webdriver import Remote


# Enable logging
logging.basicConfig(level=logging.DEBUG)

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '12'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = 'com.android.settings.SubSettings'

driver = Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(5)
driver.quit()



