import asyncio
import time

from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        bro=await p.chromium.launch()
        page=await bro.new_page()
        await page.goto("https://www.baidu.com")
        print(await page.title())
        time.sleep(3)
        await bro.close()

asyncio.run(main())