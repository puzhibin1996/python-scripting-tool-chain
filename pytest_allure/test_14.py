import allure
import pytest


def test_attach(page):
    page.goto("https://www.baidu.com/")
    png_bytes=page.screenshot()
    allure.attach(
        png_bytes,
        name="full-page",
        attachment_type=allure.attachment_type.PNG
    )
if __name__ == '__main__':
    pytest.main()