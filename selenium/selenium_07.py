from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def demo01(driver):
    driver.get("http://www.baidu.com")

def demo02(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    revealed = driver.find_element(By.ID, 'revealed')
    driver.find_element(By.ID,'reveal').click()

    wait = WebDriverWait(driver, 15)
    wait.until(lambda d: revealed.is_displayed())

    revealed.send_keys('Displayed')

    assert revealed.get_property('value') == 'Displayed'



if __name__ == '__main__':
    driver = webdriver.Edge()
    demo02(driver)