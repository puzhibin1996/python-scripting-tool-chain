from  selenium  import webdriver
# 隐式等待
edge=webdriver.Edge()
edge.get('https://www.baidu.com')
edge.implicitly_wait(2)#  隐私等待2秒
print(edge.title)
