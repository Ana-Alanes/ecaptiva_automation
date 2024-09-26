from playwright.sync_api import Page
import pytest
    
def test_tab_captiva_academy(page: Page):
    page.goto("http://192.168.1.52:5173/")
    assert page.inner_text('//*[@id="my-header"]/div[2]/div[2]/nav/ul/li[5]/a') == "CAPTIVA ACADEMY"     
    