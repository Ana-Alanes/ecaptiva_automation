import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        page = await browser.new_page()
        await page.goto("http://192.168.1.52:5173/")
        print(await page.title())
        await browser.close()
        
asyncio.run(main())