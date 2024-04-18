from playwright.sync_api import Page
import pytest

def test_tab_blog(page: Page):
    page.goto("http://192.168.1.115:5173/")
    assert page.inner_text('//*[@id="my-header"]/div[2]/div[2]/nav/ul/li[3]/a') == "BLOG"    