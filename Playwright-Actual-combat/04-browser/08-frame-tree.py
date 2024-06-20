from playwright.sync_api import Playwright,sync_playwright


def run(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://www.baidu.com")
    dump_frame_tree(page.main_frame,"")

def dump_frame_tree(frame,indent):
    # print(indent + frame.name + '@' + frame.url)
    for child in frame.child_frames:
        dump_frame_tree(child,indent + " ")
    print(indent + frame.name + '@' + frame.url)


with sync_playwright() as playwright:
    run(playwright)