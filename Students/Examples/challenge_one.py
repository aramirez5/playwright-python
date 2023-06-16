import re
from playwright.sync_api import Page, expect


def test_challenge_one(page: Page, url: str = "https://demoqa.com/"):

    # Go to main page and check title
    page.goto(url)
    expect(page).to_have_title(re.compile("DEMOQA"))

    # Click elements button 
    button_one = page.locator("text=Elements")
    button_one.click()
    page.screenshot(path="Images/step1.png")

    # Click text box button
    button_two = page.locator("text=Text Box")
    button_two.click()
    page.screenshot(path="Images/step2.png")

    # Fill form
    page.locator("#userName").fill("John Doe")
    page.locator("#userEmail").fill("johndoe@gmail.com")
    page.locator("#currentAddress").fill("Spain")
    page.locator("#permanentAddress").fill("Italy")
    page.locator("#submit").click()
    page.screenshot(path="Images/step3.png")

    # Check form
    expect(page.locator("#name")).to_have_text("Name:John Doe")
    expect(page.locator("#email")).to_have_text("Email:johndoe@gmail.com")
    expect(page.locator("//p[@id='currentAddress']")).to_have_text(
        "Current Address :Spain"
    )
    expect(page.locator("//p[@id='permanentAddress']")).to_have_text(
        "Permananet Address :Italy"
    )
    expect(page).to_have_url(re.compile(".*/text-box"))
    page.screenshot(path="Images/step4.png")