import re
from playwright.sync_api import Page, expect


def test_challenge_two(page: Page, url: str = "https://demoqa.com/checkbox"):

    # Go to main page and check title
    page.goto(url)
    expect(page).to_have_title(re.compile("DEMOQA"))
    page.screenshot(path="Images/checkbox1.png")

    # Click on the checkbox
    checkbox = page.locator("[aria-label=Toggle]")
    expect(checkbox).to_be_visible()
    checkbox.click()
    page.screenshot(path="Images/checkbox2.png")
    page.locator("[aria-label=Toggle]").nth(1).click()
    page.screenshot(path="Images/checkbox3.png")
    page.locator("text=Commands").click()
    page.screenshot(path="Images/checkbox4.png")