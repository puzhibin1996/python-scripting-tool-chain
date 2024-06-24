import time

from playwright.sync_api import Playwright,sync_playwright
def run(playwright:Playwright):
    browser=playwright.webkit.launch(headless=False)
    page=browser.new_page()
    page.goto("https://www.baidu.com/")
    # 打印浏览器的标题
    print(page.title())
    # 定位输入框 属性选择器
    page.query_selector('input[id="kw"]').fill("测试流程图")
    # 点击百度一下按钮 属性选择器
    page.query_selector('input[id="su"]').click()
    page.wait_for_timeout(3000)
    # 通过xpath定位元素
    page.query_selector('//*[@id="s_tab"]/div/a[1]').click()
    page.wait_for_timeout(3000)

with sync_playwright() as playwright:
    run(playwright)

