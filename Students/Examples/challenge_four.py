import re
import time
from playwright.sync_api import Page, expect


def test_challenge_four(page: Page, url: str = "https://datatables.net/extensions/select/examples/initialisation/checkbox"):

    # Go to main page and check title
    page.goto(url)
    expect(page).to_have_title(re.compile("DataTables example - Checkbox selection"))
    page.screenshot(path="Images/challenge_four1.png")

    # Check elements
    for i in range(1,11):
        page.locator(f"(//td[@class='  select-checkbox'])[{i}]").click()

        if i == 10:
            page.locator(f"//a[contains(@data-dt-idx,'2')]").click()

            for x in range(1,11):
                page.locator(f"(//td[@class='  select-checkbox'])[{x}]").click()

                if x == 10:
                    page.locator(f"//a[contains(@data-dt-idx,'3')]").click()

                    for y in range(1,11):
                        page.locator(f"(//td[@class='  select-checkbox'])[{y}]").click()
            
    time.sleep(0.7)        
    page.screenshot(path="Images/challenge_four2.png")