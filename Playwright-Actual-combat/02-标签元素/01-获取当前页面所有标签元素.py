import os
import subprocess

from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright



class BrowserController:
    # 初始化端口信息和playwright框架
    def __init__(self, port):
        self.port = port
        self.page = None
        self.playwright = None
        self.async_playwright=None
        self.browser = None

    # 初始化浏览器，并打开浏览器
    def start_browser(self):
        edge_command = f'start msedge --remote-debugging-port={self.port} --user-data-dir="C:/temp/msedge-user-data"'
        subprocess.Popen(edge_command, shell=True)

    # 对初始化的浏览器建立连接
    def connect_to_browser(self,url):
        self.playwright=sync_playwright().start()
        try:
            self.browser=self.playwright.chromium.connect_over_cdp(f'http://localhost:{self.port}')
            context=self.browser.contexts[0] if self.browser.contexts else self.browser.new_context()
            self.page=context.new_page()
            self.page.goto(url)
            print(f"成功建立连接并访问页面！{url}")
        except Exception as e:
            print("无法建立连接浏览器！")
            self.page=None
    # 获取当前页面所有标签元素
    def get_all_elements(self):
        if self.page:
            elements=self.page.query_selector_all("*")
            for element in elements:
                print(element.inner_html())
                print('有元素内容！')
        else:
            print("无法获取元素，请检查浏览器是否连接成功！")

    # screenshot 截图保存
    def fun_screenshot(self):
        if self.page:
            self.page.screenshot(path="img/screenshot.png")
    #
    




if __name__ == '__main__':
    port=9898
    # 初始化浏览器控制器
    controller=BrowserController(port)
    # 启动浏览器
    # controller.start_browser()# 当端口9898浏览器启动后，可以注释掉
    # 连接端口9898浏览器，进行访问百度网站
    controller.connect_to_browser("https://www.baidu.com")

    # controller.get_all_elements()
    controller.fun_screenshot()
    # controller.fun_once()
