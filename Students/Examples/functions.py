import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright

class Global_Functions:

    def __init__(self, page):
        self.page = page
    
    def Wait(self, wait_time):
        time.sleep(wait_time)

    def Scroll(self, x, y, wait_time):
        self.page.mouse.wheel(x, y)
        time.sleep(wait_time)
    
    def Text(self, select, text, wait_time):
        t = self.page.locator(select)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        expect(t).to_be_empty()
        t.highlight()
        t.fill(text)
        time.sleep(wait_time)

    def Text_img(self, select, text, path, wait_time):
        t = self.page.locator(select)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        expect(t).to_be_empty()
        t.highlight()
        t.fill(text)
        self.page.screenshot(path=path)
        time.sleep(wait_time)

    def Click(self, select, wait_time):
        t = self.page.locator(select)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        t.highlight()
        t.click()
        time.sleep(wait_time)

    def Combo_value(self, select, value, wait_time):
        t = self.page.locator(select)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        t.highlight()
        t.select_option(value)
        time.sleep(wait_time)
    
    def Combo_label(self, select, value, wait_time):
        t = self.page.locator(select)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        t.highlight()
        t.select_option(label=value)
        time.sleep(wait_time)

    def Check_title(self, text, wait_time):
        expect(self.page).to_have_title(text)
        time.sleep(wait_time)
    
    def Check_url(self, text, wait_time):
        expect(self.page).to_have_url(re.compile(text))
        time.sleep(wait_time)

    def Check_text(self, select, text, wait_time):
        t = self.page.locator(select)
        expect(t).to_contain_text(text)
        time.sleep(wait_time)
    
    def Press_tab_key(self, wait_time):
        self.page.keyboard.press("Tab")
        time.sleep(wait_time)

    def Upload_file(self, select, file, wait_time):
        self.page.locator(select).set_input_files(file)
        time.sleep(wait_time)

    def Upload_file_remove(self, select, wait_time):
        self.page.locator(select).set_input_files([])
        time.sleep(wait_time)