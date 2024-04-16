from playwright.sync_api import Page
import pytest

def test_tab_company(page: Page):
    page.goto("https://captivasoft.net")
    assert page.inner_text('//*[@id="my-header"]/div[2]/div[2]/nav/ul/li[1]/a') == "COMPANY" 