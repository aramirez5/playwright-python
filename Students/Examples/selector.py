import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from functions import Global_Functions

#Global variables
time_wait = 0.5
path = "Images/"

#def test_challenge_two(page: Page, url: str = "https://testingqarvn.com.es/datos-personales/"):
def test_selector(playwright: Playwright, url: str = "https://testingqarvn.com.es/combobox/") -> None:

    #Config
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(
        viewport={"width": 1280, "height": 720}
    )
    page = context.new_page()

    # Go to main page and check title
    page.goto(url)
    gf = Global_Functions(page)
    gf.Check_title("ComboBox | TestingQaRvn", time_wait)
    page.screenshot(path="Images/selector1.png")

    #Scroll
    gf.Scroll(0, 400, time_wait)
    
    #Wait
    gf.Wait(time_wait)

    #Fill the form
    gf.Text_img("//input[contains(@id,'wsf-1-field-45')]", "John", path+"selector2.png", time_wait)
    gf.Text("//input[contains(@id,'wsf-1-field-46')]", "Doe", time_wait)
    gf.Text("//input[contains(@id,'wsf-1-field-47')]", "john.doe@gmail.com", time_wait)
    gf.Text("//input[contains(@id,'wsf-1-field-48')]", "666666666", time_wait)
    gf.Text("//textarea[@id='wsf-1-field-49']", "Testing Street", time_wait)
    gf.Click("(//label[contains(@class,'wsf-label')])[7]", time_wait)
    gf.Click("//label[contains(@id,'wsf-1-label-51-row-1')]", time_wait)
    gf.Combo_value("//select[contains(@id,'wsf-1-field-53')]", "Linux", time_wait)
    gf.Combo_label("//select[contains(@id,'wsf-1-field-53')]", "Mac", time_wait)

    #Submit
    gf.Click("#wsf-1-field-52", time_wait)

    #Check url
    gf.Check_url("https://testingqarvn.com.es/combobox/", time_wait)

    #Check message
    gf.Check_text("//p[contains(text(),'Gracias por tu encuesta.')]", "Gracias", time_wait)