from playwright.sync_api import Playwright, sync_playwright




def on_download(download):
    print(f"Download will begin to: {download.suggested_filename}")
    download.save_as("./downloads/" + download.suggested_filename)


def fun(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    # page.on("download", on_download)
    # page.get_by_text("Download file").click()
    # download=download_info.value
    # Start waiting for the download
    with page.expect_download() as download_info:
        # Perform the action that initiates download
        page.get_by_text("Download file").click()
    download = download_info.value

    # Wait for the download process to complete and save the downloaded file somewhere
    download.save_as("/path/to/save/at/" + download.suggested_filename)



with sync_playwright() as playwright:
    fun(playwright)

