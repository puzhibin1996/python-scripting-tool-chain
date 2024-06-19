import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://www.baidu.com/")

    # Expect a title "to contain" a substring.
    if page.title() != "百度一下，你就知道":
        print("title is not baidu")
        print(page.title())
    expect(page).to_have_title(re.compile("百度"))

def test_get_started_link(page: Page):
    page.goto("https://www.baidu.com/")

    # Click the get started link.
    page.get_by_role("link", name="百度一下").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()