from playwright.sync_api import Page
import pytest 


def browser():
    with Page() as p:
        browser = p.chromium.launch()
        browser.close()

def test_click_button(browser):
    page = browser.new_page()
    page.goto('http://192.168.1.52:5173/')
    page.click('//*[@id="my-header"]/div[2]/div[2]/nav/ul/li[1]/a')
    page.close()


def test_tab_company(page: Page):
    page.goto("http://192.168.1.115:5173/")
    assert page.inner_text('//*[@id="my-header"]/div[2]/div[2]/nav/ul/li[1]/a') == "COMPANY" 
  
def test_container_server_as(page: Page):
    page.goto("http://192.168.1.115:5173/company")
    assert page.inner_text('//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div/div[1]/h1') =="WE SERVE AS YOUR DIGITAL SPEED-UP ALLY." 

def test_container_ceo_menssage(page: Page):
    page.goto("http://192.168.1.115:5173/company")
    expected_text = "Through high-end processes and engineers, we provide the service and transparency our clients need."
    assert page.inner_text('//*[@id="root"]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/h3') == expected_text
    
def test_container_brands_that_trust_as(page: Page):
    page.goto("http://192.168.1.115:5173/company")
    assert page.inner_text('//*[@id="root"]/div/div[2]/div/div/div[3]/div/div/div[2]/div[1]') =="BRANDS THAT TRUST US"

def test_container_captiva_true_story(page : Page):
     page.goto("http://192.168.1.115:5173/company")
     assert page.inner_text('//*[@id="root"]/div/div[2]/div/div/div[4]/div/div[2]/div[1]/h2') =="CAPTIVA true story"

