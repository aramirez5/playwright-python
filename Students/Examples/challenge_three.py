import re
import time
from playwright.sync_api import Page, expect


def test_challenge_three(page: Page, url: str = "https://testingqarvn.com.es/prueba-de-campos-checkbox/"):

    # Go to main page and check title
    page.goto(url)
    expect(page).to_have_title(re.compile("Prueba de campos Checkbox | TestingQaRvn"))
    page.screenshot(path="Images/challenge_three1.png")

    # Fill form
    page.locator("#wsf-1-field-29").fill("John")
    page.locator("#wsf-1-field-30").fill("Doe")
    page.locator("#wsf-1-field-31").fill("johndoe@gmail.com")
    page.locator("#wsf-1-field-32").fill("666666666")
    page.locator("#wsf-1-field-33").fill("Testing Street")
    
    # Check options
    # page.get_by_text("PHP").check()
    # page.get_by_text("PYTHON", exact=True).click()
    # page.get_by_text("JS").check()
    # page.get_by_text("PHP").uncheck()
    # assert page.get_by_text("JS").is_checked() == True
    for i in range(7,10):
        page.locator(f"(//label[contains(@class,'wsf-label')])[{i}]").click()
        time.sleep(1)
    
    # Send form
    button=page.locator("#wsf-1-field-34")
    button.click()
    page.screenshot(path="Images/challenge_three2.png")

    # Check form
    expect(page.locator(
        "//p[contains(text(),'Gracias por tu encuesta.')]")
    ).to_contain_text("Gracias")
    page.screenshot(path="Images/challenge_three3.png")