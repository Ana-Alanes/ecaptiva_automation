from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://captivasoft.net")
    page.get_by_role("link", name="SERVICES", exact=True).click()
    page.get_by_role("link", name="COMPANY", exact=True).click()
    page.get_by_role("link", name="BLOG", exact=True).click()
    page.get_by_role("link", name="Volver al Home").click()
    page.get_by_role("link", name="CAREERS", exact=True).click()
    page.get_by_role("link", name="CAPTIVA ACADEMY", exact=True).click()
    page.get_by_role("link", name="Volver al Home").click()
    page.get_by_role("link", name="GET AN ESTIMATE", exact=True).click()
    page.get_by_role("link", name="Logo Captiva").click()
