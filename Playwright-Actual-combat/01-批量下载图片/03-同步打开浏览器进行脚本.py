import subprocess
import time
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

    def perform_actions(self):
        if self.page:
            # 在这里执行点击事件或其它事件
            self.page.click('kw')  # 替换为实际的选择器
            print("Performed actions on the page")

    def close(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()

if __name__ == '__main__':
    port = 6666
    controller = BrowserController(port)
    controller.start_playwright()
    time.sleep(3)  # 等待浏览器启动完成
    controller.connect_to_browser_and_visit_url('https://www.baidu.com')
    # if controller.page:
    #     controller.perform_actions()
    #     input("Press Enter to close the browser...")
    # controller.close()
