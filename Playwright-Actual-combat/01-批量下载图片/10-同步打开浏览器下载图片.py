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
    # def perform_actions(self):
    #     if self.page:
    #         # 在这里执行点击事件或其它事件
    #         self.page.click('kw')  # 替换为实际的选择器
    #         print("Performed actions on the page")
    #
    # def close(self):
    #     if self.browser:
    #         self.browser.close()
    #     if self.playwright:
    #         self.playwright.stop()

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

    def download_img(self):
        if self.page:
            image_elements=self.page.query_selector_all('img')
            image_urls=[img.get_attribute('src') for img in image_elements]

            os.makedirs('./images', exist_ok=True)
            # 下载图片
            for idx, img_url in enumerate(image_urls):
                if img_url:
                    try:
                        img_data = requests.get(img_url).content
                        # 确定图像扩展名
                        ext = img_url.split('.')[-1]
                        if '?' in ext:
                            ext = ext.split('?')[0]
                        with open(f'downloaded_images/image_{idx}.{ext}', 'wb') as handler:
                            handler.write(img_data)
                        print(f"Downloaded image_{idx}.{ext}")
                    except Exception as e:
                        print(f"Failed to download {img_url}: {e}")





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
        controller.download_img()


