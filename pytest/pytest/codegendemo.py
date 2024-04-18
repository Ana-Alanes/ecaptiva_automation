import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("http://192.168.1.115:5173/")
    page.get_by_role("link", name="COMPANY", exact=True).click()
    page.get_by_role("heading", name="WE SERVE AS YOUR DIGITAL").click()
    page.get_by_role("heading", name="We offer the best in software").click()
    page.get_by_role("heading", name="Through high-end processes").click()
    page.get_by_role("heading", name="Christian Alvaro Avila Perez –").click()
    page.get_by_role("heading", name="BRANDS THAT TRUST US").click()
