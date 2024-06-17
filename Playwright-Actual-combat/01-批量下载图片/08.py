from playwright.sync_api import sync_playwright

playwright=sync_playwright().start()

b=playwright.chromium.launch()
page=b.new_page()
page.goto("https://www.baidu.com/")
page.get_by_role("kw").fill("测试台架")

b.close()
playwright.stop()