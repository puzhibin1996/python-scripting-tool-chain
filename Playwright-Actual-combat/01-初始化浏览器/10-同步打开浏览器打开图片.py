import os
import subprocess
import time

import requests
from playwright.sync_api import sync_playwright


class BrowserController:
    def __init__(self, port):
        self.port = port
        self.page = None
        self.playwright = None
        self.browser = None

    def start_playwright(self):
        edge_command = f'start msedge --remote-debugging-port={self.port} --user-data-dir="C:/temp/msedge-user-data"'
        subprocess.Popen(edge_command, shell=True)

    def connect_to_browser_and_visit_url(self, url):
        self.playwright = sync_playwright().start()
        try:
            self.browser = self.playwright.chromium.connect_over_cdp(f'http://localhost:{self.port}')
            context = self.browser.contexts[0] if self.browser.contexts else self.browser.new_context()
            self.page = context.new_page()
            self.page.goto(url)
            print(f'Visited {url} on port {self.port}')
        except Exception as e:
            print(f"Failed to connect to browser: {e}")
            self.page = None

    def input_text(self):
        if self.page:
            search_input = self.page.query_selector('input[name="wd"]')
            if search_input:
                search_input.fill('测试流程图')

    def input_btn(self):
        if self.page:
            search_btn = self.page.query_selector('input[name="submit"]')
            if search_btn:
                search_btn.click()
    # 鼠标滑动
    def scrollTo_move(self):
        if self.page:
            # 鼠标滑动
            # self.page.evaluate('window.scrollTo(0, document.body.scrollHeight)')# 滑动到页面底部
            self.page.evaluate('window.scrollTo(0,5)')# 滚动到500 像素位置
            print("Mouse moved to the bottom of the page")

    def get_img(self):
        if self.page:
            self.page.query_selector('//*[@id="1"]/div/h3/a').click()


if __name__ == '__main__':
    port = 6666
    controller = BrowserController(port)
    controller.start_playwright()
    time.sleep(3)  # 等待浏览器启动完成
    controller.connect_to_browser_and_visit_url('https://www.baidu.com')
    if controller.page:
        controller.input_text()
        controller.input_btn()
        time.sleep(2)
        controller.scrollTo_move()
        controller.get_img()


