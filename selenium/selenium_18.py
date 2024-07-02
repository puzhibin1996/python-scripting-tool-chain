from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url=  "https://www.selenium.dev/documentation/webdriver/interactions/alerts/"
driver = webdriver.Edge()
driver.get(url)
element = driver.find_element(By.LINK_TEXT,"See a sample prompt")
driver.execute_script("arguments[0].click();",element)
wait = WebDriverWait(driver,timeout=2)
alert = wait.until(lambda driver: driver.switch_to.alert)
alert.send_keys("Selenium")
text = alert.text
print(text)
alert.accept()

