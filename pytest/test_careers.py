from playwright.sync_api import Page
import pytest

def test_tab_careers(page: Page):
    page.goto("http://192.168.1.52:5173/")
    assert page.inner_text('//*[@id="my-header"]/div[2]/div[2]/nav/ul/li[4]/a') == "CAREERS"
    
 
def test_description_careers(page: Page):
    page.goto("http://192.168.1.52:5173/")
    page.get_by_role('//*[@id="my-header"]/div[2]/div[2]/nav/ul/li[4]/a').click()   
    assert page.inner_text('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/h2') == "Work Remotely"
    
    