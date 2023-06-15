import re
import time
import random
import pytest
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from functions import Global_Functions
from config_test import *

# Global variables
time_wait = 0.5
path = "Images/"
pdf = "C:/laragon/www/playwright-python/Students/Examples/Documents/sample.pdf"
url = "https://testingqarvn.com.es/datos-personales/"

@pytest.fixture(scope="function")
def set_up_excel(playwright: Playwright) -> None:
    
    # Config
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(
        viewport={"width": 1280, "height": 720}
    )
    page = context.new_page()

    # Go to main page and check title
    page.goto(url)

    yield page

    # Close context and browser
    context.close()
    browser.close()
