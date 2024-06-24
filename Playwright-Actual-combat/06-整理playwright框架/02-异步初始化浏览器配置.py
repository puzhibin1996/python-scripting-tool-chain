import asyncio

from playwright.async_api import Playwright,async_playwright
async def run(playwright:Playwright):
    browser= await playwright.chromium.launch(headless=False)
    page= await browser.new_page()
    await page.goto('https://baidu.com')
    print(await page.title())
async def main():
    async  with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())