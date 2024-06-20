import time

from playwright.sync_api import Playwright,sync_playwright


def handle_dialog(dialog):
    print(dialog.message)
    dialog.dismiss()

def fun(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.on("dialog",handle_dialog)
    # a dialog box is displayed on the browser page
    page.evaluate("alert('1234567890')")
    browser.close()

with sync_playwright() as playwright:
    fun(playwright)