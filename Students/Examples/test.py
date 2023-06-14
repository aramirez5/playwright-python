import re
from playwright.sync_api import Page, expect


def test(page: Page, url: str = "https://playwright.dev/"):
    """
    This function navigates to the Playwright intro page, clicks the "Get started" button, and checks
    that the page title and URL are correct.

    :param page: The current page object that the function will interact with. It is likely an instance
    of a Playwright Page class
    :type page: Page
    :param url: The URL of the website to navigate to. In this case, it is set to
    "https://playwright.dev/", defaults to https://playwright.dev/
    :type url: str (optional)
    """

    # Go to main page and check title
    page.goto(url)
    expect(page).to_have_title(re.compile("Playwright"))

    # Click button
    button = page.locator("text=Get started")
    expect(button).to_have_attribute("href", "/docs/intro")
    page.screenshot(path="Images/screenshot_before.png")
    button.click()

    # Check elements
    page.screenshot(path="Images/screenshot_after.png")
    expect(page).to_have_title(re.compile("Playwright"))
    expect(page).to_have_url(re.compile(".*/docs/intro"))
