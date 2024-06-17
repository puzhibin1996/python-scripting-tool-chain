from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    bro=p.chromium.launch(headless=False,slow_mo=50)
    page=bro.new_page()
    page.goto('https://playwright.dev/')
    page.screenshot(path='img/1.png')
    bro.close()