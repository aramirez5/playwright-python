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
url1 = "https://testingqarvn.com.es/upload-files/"
url2 = "https://www.saucedemo.com/"
url3 = "https://testingqarvn.com.es/datos-personales/"

@pytest.fixture(scope="function")
def set_up(playwright: Playwright) -> None:
    
    # Config
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(
        viewport={"width": 1280, "height": 720}
    )
    page = context.new_page()

    # Go to main page and check title
    page.goto(url1)

    yield page

    # Close context and browser
    context.close()
    browser.close()

@pytest.fixture(scope="session")
def set_up_demo(playwright: Playwright) -> None:
    
    # Config
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(
        viewport={"width": 1280, "height": 720}
    )
    page = context.new_page()

    # Go to main page and check title
    page.goto(url2)

    # Login
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    yield page

    # Close context and browser
    context.close()
    browser.close()

@pytest.fixture(scope="session")
def set_up_session_username(playwright: Playwright) -> None:
    
    # Config
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(
        viewport={"width": 1280, "height": 720}
    )
    page = context.new_page()

    # Go to main page and check title
    page.goto(url2)

    # Login
    page.locator("[data-test=\"username\"]").fill("standard_user2")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    yield page

    # Close context and browser
    context.close()
    browser.close()

@pytest.fixture(scope="session")
def set_up_session_password(playwright: Playwright) -> None:
    
    # Config
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(
        viewport={"width": 1280, "height": 720}
    )
    page = context.new_page()

    # Go to main page and check title
    page.goto(url2)

    # Login
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce2")
    page.locator("[data-test=\"login-button\"]").click()

    yield page

    # Close context and browser
    context.close()
    browser.close()

@pytest.fixture(scope="function")
def set_up_parametrized(playwright: Playwright) -> None:
    
    # Config
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(
        viewport={"width": 1280, "height": 720}
    )
    page = context.new_page()

    # Go to main page and check title
    page.goto(url3)

    yield page

    # Close context and browser
    context.close()
    browser.close()