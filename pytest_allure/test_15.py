from pathlib import Path

import allure
import pytest


def test_attach_file(page):
    page.goto("https://www.baidu.com/")
    png_bytes=page.screenshot()
    Path("full-page.png").write_bytes(png_bytes)
    allure.attach.file(
        "full-page.png",
        name="full-page",
        attachment_type=allure.attachment_type.PNG
    )

if __name__ == '__main__':
    pytest.main()