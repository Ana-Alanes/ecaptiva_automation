from playwright.sync_api import Page
import pytest

def test_tab_company(page: Page):
    page.goto("http://192.168.1.115:5173/")
    assert page.inner_text('//*[@id="my-header"]/div[2]/div[2]/nav/ul/li[1]/a') == "COMPANY" 

def test_Work_Remotely(page: Page):
    page.goto("http://192.168.1.115:5173/")
    assert page.inner_text('//*[@id="h3-min-height"]') == "BRANDS THAT TRUST US" 