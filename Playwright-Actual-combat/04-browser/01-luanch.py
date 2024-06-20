from playwright.sync_api import Playwright,sync_playwright



# 通过调用 luanch() 创建，并使用浏览器创建主页

def fun(playwright:Playwright):
    w=playwright.webkit
    browser=w.launch(headless=False)
    # init browser new page
    page=browser.new_page()
    # go to url locating page
    page.goto("https://baidu.com")
    # off browser
    page.close()

if __name__ == '__main__':
    with sync_playwright() as playwright:
        #  fun
        fun(playwright)
