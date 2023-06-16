import re
import time
from playwright.sync_api import expect, Playwright

url = "https://testingqarvn.com.es/datos-personales/"

#def test_challenge_two(page: Page, url: str = "https://testingqarvn.com.es/datos-personales/"):
def test_challenge_two(
        playwright: Playwright, 
        url: str = url
    ) -> None:

    #Config
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    context = browser.new_context(
        viewport={"width": 1280, "height": 720}
    )
    context = browser.new_context(record_video_dir="Videos")
    page = context.new_page()

    # Go to main page and check title
    page.goto(url)
    expect(page).to_have_title(re.compile("Datos Personales | TestingQaRvn"))
    page.screenshot(path="Images/challenge_two1.png")

    # Fill form
    page.locator("#wsf-1-field-21").fill("John")
    page.locator("#wsf-1-field-22").fill("Doe")
    page.locator("#wsf-1-field-23").fill("johndoe@gmail.com")
    page.locator("#wsf-1-field-24").fill("666666666")
    page.locator("#wsf-1-field-28").fill("Testing Street")
    button=page.locator("#wsf-1-field-27")
    expect(button).to_be_visible()
    expect(button).to_be_enabled()
    if button:
        button.click()
    else:
        print("Button not found")
    page.screenshot(path="Images/challenge_two2.png")

    # Check form
    expect(page.locator(
        "//p[contains(text(),'Gracias por tu encuesta.')]")
    ).to_contain_text("Gracias")
    expect(page).to_have_url(re.compile(".*/datos-personales"))
    time.sleep(2)
    page.screenshot(path="Images/challenge_two3.png")