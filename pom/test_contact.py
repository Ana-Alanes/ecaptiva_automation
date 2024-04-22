from playwright.sync_api import sync_playwright
from pageObjects.searchPage import searchPage

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    search_page = searchPage(page)

    search_page.navigate()
    search_page.search("JuanPerez", "juanmail.com", "60776212", "Test", "test")

    page.screenshot(path="contact.png")
    print(page.title())
    browser.close()