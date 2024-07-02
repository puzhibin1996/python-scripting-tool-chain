import time

from selenium import webdriver


options = webdriver.EdgeOptions()
# options.add_argument('--start-maximized') # 设置为最大窗口化

options.add_experimental_option("detach",True)# 设置窗口保持打开状态，不会在执行完程序就关闭

driver =webdriver.Edge(options=options)




# time.sleep(3)
