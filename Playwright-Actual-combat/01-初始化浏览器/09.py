import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    bro = p.chromium.launch(executable_path=edge_path, headless=False)
    page = bro.new_page()
    page.goto("https://www.baidu.com")

    # 输入搜索关键词
    search_input = page.query_selector('input[name="wd"]')
    if search_input:
        search_input.fill("Playwright")
        print("Filled search input")

    # 点击搜索按钮
    search_button = page.query_selector('input[type="submit"]')
    if search_button:
        search_button.click()
        print("Clicked search button")

    time.sleep(5)  # 等待几秒钟查看结果
    page.close()
    bro.close()
