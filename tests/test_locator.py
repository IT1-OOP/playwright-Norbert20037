import os
from playwright.sync_api import sync_playwright, expect
import urllib.parse

def test_page_title():
    file_path = os.path.abspath("./src/index.html")
    file_path = urllib.parse.unquote(file_path)
    print(file_path)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"file:///{file_path}")
        nadpis_1 = page.locator('h1').first
        nadpis_text = page.locator('text="Nadpis 1"')
        div_1 = page.locator('.container')
        expect(nadpis_1).to_be_visible()
        expect(nadpis_text).to_be_visible()
        expect(div_1).to_be_visible()
        expect(nadpis_text).to_have_count(1)
        w3_link = page.locator('#w3link')
        expect(w3_link).to_be_visible()
        w3_link.click() 
        browser.close()