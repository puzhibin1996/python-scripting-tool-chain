from playwright.sync_api import sync_playwright

playwright=sync_playwright().start()

b=playwright.chromium.launch()
page=b.new_page()
page.goto("https://playwright.dev/")
page.screenshot(path="img/2.png")
b.close()
playwright.stop()