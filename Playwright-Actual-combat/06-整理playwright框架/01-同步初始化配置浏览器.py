import time

from playwright.sync_api import Playwright,sync_playwright
def run(playwright :Playwright):
    browser=playwright.chromium.launch(headless=False)# 定义有头浏览器，可以显示看到浏览器基本操作
    page=browser.new_page()
    page.goto("https://www.baidu.com/")
    print(page.title())
    time.sleep(3)

with sync_playwright() as playwright:
    run(playwright)



