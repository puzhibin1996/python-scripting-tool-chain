import time

from playwright.sync_api import Playwright,sync_playwright


def run(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    page.goto("https://github.com/login")
    page.get_by_label("Username or email address").fill("username")
    page.get_by_label("Password").fill("password")
    page.get_by_role("button",name="Sign in").click()
    time.sleep(5)



with sync_playwright() as playwright:
    run(playwright)