import time

from  playwright.sync_api import sync_playwright

with sync_playwright() as p:
    bro=p.chromium.launch()
    page=bro.new_page()
    page.goto("https://www.baidu.com/")
    print(page.title())
    time.sleep(3)
    bro.close()