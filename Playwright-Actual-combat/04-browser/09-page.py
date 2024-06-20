from playwright.sync_api import Playwright,sync_playwright


def run(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://www.baidu.com")
    page.screenshot(path=".img/baidu.png")
    page.on("request",log_request)

    # page.remove_listener("request1",log_request)

def log_request(intercepte_request):
    print("a request was made:",intercepte_request.url)


with sync_playwright() as playwright:
    run(playwright)
