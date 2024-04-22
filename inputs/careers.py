import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        await page.set_viewport_size({"width": 1800, "height": 1200})
        await page.goto("http://192.168.1.115:5173/")

        await page.click('//*[@id="my-header"]/div[2]/div[2]/nav/ul/li[4]/a')
        await page.screenshot(path="screenshots/careers.png")

        await exec(page.locator("#result")).to_have_text("BECOME A CAPTIVA ENGINEER")

        await page.click('//*[@id="my-header"]/div[2]/div[2]/nav/ul/li[4]/a')
        await page.screenshot(path="screenshots/careerswork.png")

        await exec(page.locator("#result")).to_have_text("Work Remotely")

        await context.tracing.stop(path="logs/trace.zip")

        await browser.close()

asyncio.run(main())