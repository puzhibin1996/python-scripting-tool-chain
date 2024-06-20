from playwright.sync_api import Playwright,sync_playwright


def fun(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://www.baidu.com")
    # page.query_selector_all("*")# *表示所有元素
    # 打印所有元素
    # for i in page.query_selector_all("*"):
    #     # print(i.inner_text())
    #     print(i.inner_html())
    with page.expect_file_chooser() as fc_info:
        page.get_by_text("Upload file").click()
    file_chooser=fc_info.value
    file_chooser.set_files("myfile.pdf")


with sync_playwright() as playwright:
    fun(playwright)