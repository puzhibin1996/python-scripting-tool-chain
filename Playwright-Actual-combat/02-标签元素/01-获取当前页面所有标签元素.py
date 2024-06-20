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
    # 打开网页版抖音
    def fun_douyin(self):
        if self.page:
            self.page.goto("https://www.douyin.com/")

    # 对当前页面进行截图
    def fun_once(self):
        if self.page:
            self.page.screenshot(path="img/douyin.png")
            print("成功截图！")
        else:
            print("无法截图，请检查浏览器是否连接成功！")

    # 对当前标签进行点击 //*[@id="login-pannel"]/div[2]
    def fun_click(self):
        if self.page:
            self.page.click("//*[@id=\"login-pannel\"]/div[2]")
            print("成功点击！")
        else:
            print("无法点击，请检查浏览器是否连接成功！")

    # 触发鼠标滚轮 上下滚轮
    def fun_scroll(self):
        if self.page:
            self.page.mouse.wheel(0, 1000)
            print("成功触发鼠标滚轮！")
        else:
            print("无法触发鼠标滚轮，请检查浏览器是否连接成功！")
    # 当前页面取消禁音状态。
    def fun_unmute(self):
        if self.page:
            self.page.evaluate("document.querySelector('video').muted=false")# 这里是js代码块，所以需要用evaluate方法执行
            print("成功取消禁音状态！")
        else:
            print("无法取消禁音状态，请检查浏览器是否连接成功！")

    # 当前视频停留15秒，然后鼠标滚轮滚轮切换下面一条视频
    def fun_scroll_next(self):
        if self.page:
            self.page.wait_for_timeout(15000)
            self.page.mouse.wheel(0, 1000)
            self.page.mouse.wheel(1000, 2000)
            print("成功触发鼠标滚轮！")
        else:
            print("无法触发鼠标滚轮，请检查浏览器是否连接成功！")


if __name__ == '__main__':
    port=9898
    # 初始化浏览器控制器
    controller=BrowserController(port)
    # 启动浏览器
    # controller.start_browser()# 当端口9898浏览器启动后，可以注释掉
    # 连接端口9898浏览器，进行访问百度网站
    controller.connect_to_browser("https://www.baidu.com")

    # controller.get_all_elements()
    # controller.fun_screenshot()
    # controller.fun_once()
    controller.fun_douyin()
    controller.fun_once()
    # controller.fun_click()
    controller.fun_scroll()
    controller.fun_unmute()
    controller.fun_scroll_next()