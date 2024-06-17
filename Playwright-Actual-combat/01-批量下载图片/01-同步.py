import time

from playwright.sync_api import Playwright, sync_playwright
def run(playwright:Playwright):
    # 指定你要打开的浏览器，当前属于隐私模式打开浏览器。
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    user_data_dir=r"C:\Program Files (x86)\Microsoft\Edge\Application\User Data"

    chromium=playwright.chromium
    browser=chromium.launch(executable_path=edge_path,headless=False)
    page=browser.new_page()
    page.goto("https://www.baidu.com/")
    time.sleep(5)
    browser.close()
with sync_playwright() as playwright:
    run(playwright)