from playwright.sync_api import Page, sync_playwright,Playwright



def run(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    contex=browser.new_context()
    page=contex.new_page()
    page.goto('https://baidu.com')
    page.route("**/*",handle)

def handle(route,request):
    headers={
        **request.headers,
        "foo":"foo-value",
        "bar":None
    }
    route.continue_(headers=headers)

# page.route("**/*",handle)

with sync_playwright() as playwright:
    run(playwright)