from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://192.168.1.52:5173/")
    page.screenshot(path="demo.png")
    browser.close()