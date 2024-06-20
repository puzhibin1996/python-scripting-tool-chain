from playwright.sync_api import Playwright, sync_playwright


def fun(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://www.baidu.com")
    # print connected or not
    print(browser.is_connected())
    # print browser version
    print(browser.version)




if __name__ == '__main__':
    with sync_playwright() as playwright:
        fun(playwright)