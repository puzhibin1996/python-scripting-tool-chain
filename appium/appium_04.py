from appium import webdriver

# Define the desired capabilities
desired_caps = {
    "platformName": "Android",
    "deviceName": "YourDeviceName",
    "appPackage": "your.app.package",
    "appActivity": "your.app.activity",
    "automationName": "UiAutomator2"
}

# Connect to the Appium server
driver = webdriver.Remote('http://127.0.0.1:4723', desired_caps)

# Now you can interact with your app
# For example, find an element and perform a click
element = driver.find_element_by_id("element_id")
element.click()

# Close the session
driver.quit()
