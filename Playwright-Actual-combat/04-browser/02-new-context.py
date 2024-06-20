from playwright.sync_api import Playwright,sync_playwright


def fun(playwright : Playwright):
    # init browser
    browser=playwright.chromium.launch(headless=False)
    # browser new context
    context=browser.new_context()
    # new context new page
    page=context.new_page()
    # go to url
    page.goto("https://www.baidu.com/")

if __name__ == '__main__':
    with sync_playwright() as playwright:
        fun(playwright)

