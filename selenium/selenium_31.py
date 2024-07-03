from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.virtual_authenticator import VirtualAuthenticatorOptions
import time

# 设置 WebDriver 的路径
webdriver_path = "path/to/msedgedriver"  # 替换为实际路径
service = Service(webdriver_path)

# 设置浏览器选项
options = Options()
options.use_chromium = True

# 启动 Edge 浏览器
driver = webdriver.Edge()

# 创建虚拟身份验证器
virtual_authenticator_options = VirtualAuthenticatorOptions()
virtual_authenticator_options.is_user_verified = True
virtual_authenticator_options.protocol = VirtualAuthenticatorOptions.Protocol.U2F
virtual_authenticator_options.transport = VirtualAuthenticatorOptions.Transport.USB
authenticator = driver.add_virtual_authenticator(virtual_authenticator_options)

# 访问需要身份验证的网页
driver.get("https://dbbp.net/category/it/ai")

driver.find_element(By.XPATH,"/html/body/div[6]/a/i").click()
# 模拟注册和验证流程
# 这里假设网站提供了 WebAuthn 注册和登录功能
register_button = driver.find_element(By.XPATH, "/html/body/header/div/ul[2]/li[3]/a[1]")
register_button.click()

time.sleep(2)

username_input = driver.find_element(By.NAME, "user_login")
username_input.send_keys("puzhibin")

userpassword_input = driver.find_element(By.NAME, "password")
userpassword_input.send_keys("1075057376@qq.com")


register_submit = driver.find_element(By.NAME, "submit")
register_submit.click()

time.sleep(2)

# 模拟登录流程
login_button = driver.find_element(By.ID, "login")
login_button.click()

time.sleep(2)

username_input = driver.find_element(By.NAME, "username")
username_input.send_keys("test_user")

login_submit = driver.find_element(By.ID, "login-submit")
login_submit.click()

time.sleep(2)

# 检查是否登录成功
assert "Welcome, test_user" in driver.page_source

# 关闭浏览器
driver.quit()
