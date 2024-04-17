import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        
        await page.set_viewport_size({"width": 1800, "height": 1200})
        await page.goto("https://captivasoft.net")
        
        #-Actions
        await page.check('//*[@id="grid-row"]/div[2]/div/div[2]/div[1]')
        await page.screenshot(path="screenshots/checkboxes.png")

        #-Assertions
        await page.is_checked('//*[@id="grid-row"]/div[2]/div/div[2]/div[1]') is True
        await expect(page.locator("#result")).to_have_text("We provide you with the latest in software development to ensure your company is always at the forefront.")

        #-Stoping Tracing
        await context.tracing.stop(path = "logs/trace.zip")

        #-Closing browser
        await browser.close()
        
asyncio.run(main())