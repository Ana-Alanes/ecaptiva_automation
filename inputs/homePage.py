from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        await page.set_viewport_size({"width": 1800, "height": 1200})
        await page.goto("http://192.168.1.52:5173/")

        await page.click('//*[@id="my-header"]/div[2]/div[1]/a/img')
        await page.screenshot(path="screenshots/homePage.png")

        await page.is_checked('//*[@id="grid-row"]') is True
        await exec(page.locator("#result")).to_have_text("Brilliant minds build great products. We have them.")
        
        await context.tracing.stop(path= "logs/trace.zip")

        await browser.close()
        
asyncio.run(main())