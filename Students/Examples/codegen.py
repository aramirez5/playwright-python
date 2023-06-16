from playwright.sync_api import Playwright

# Global variables
time_wait = 0.5
path = "Images/"
url = "https://www.saucedemo.com/"

def test_codegen(playwright: Playwright, url: str = url) -> None:

    # Config
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context(
        viewport={"width": 1280, "height": 720}
    )
    page = context.new_page()

    # Go to main page and check title
    page.goto(url)
    
    # Login
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
  
    # Add item to cart
    page.locator("#item_4_title_link").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("a").filter(has_text="1").click()
    page.locator("[data-test=\"checkout\"]").click()
