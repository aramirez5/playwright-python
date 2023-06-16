import random
from playwright.sync_api import Playwright
from functions import Global_Functions

#Global variables
time_wait = 0.5
path = "Images/"
url = "https://testingqarvn.com.es/combobox-dependiente/"

#def test_challenge_two(page: Page, url: str = "https://testingqarvn.com.es/datos-personales/"):
def test_selector_two(playwright: Playwright, url: str = url) -> None:

    #Config
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(
        viewport={"width": 1280, "height": 720}
    )
    page = context.new_page()

    # Go to main page and check title
    page.goto(url)
    gf = Global_Functions(page)
    gf.Check_title("ComboBox Dependiente | TestingQaRvn", time_wait)
    page.screenshot(path="Images/selector_two1.png")

    #Scroll
    gf.Scroll(0, 400, time_wait)
    
    #Wait
    gf.Wait(time_wait)

    #Fill the form
    gf.Text_img("#wsf-1-field-54", "John", path+"selector_two2.png", time_wait)
    gf.Text("#wsf-1-field-55", "Doe", time_wait)
    gf.Text("#wsf-1-field-56", "john.doe@gmail.com", time_wait)
    gf.Text("#wsf-1-field-57", "666666666", time_wait)
    gf.Text("#wsf-1-field-58", "Testing Street", time_wait)
    gf.Click("#wsf-1-label-59-row-1", time_wait)
    gf.Click("#wsf-1-label-60-row-1", time_wait)

    #Combobox
    gf.Combo_value("#wsf-1-field-61", "Linux", time_wait)
    num = random.sample(range(1, 4), 1)
    if num[0] == 1:
        gf.Combo_label("#wsf-1-field-64", "Ubuntu", time_wait)
    elif num[0] == 2:
        gf.Combo_label("#wsf-1-field-64", "Debian", time_wait)
    elif num[0] == 3:
        gf.Combo_label("#wsf-1-field-64", "Read Hat", time_wait)

    #Submit
    gf.Click("#wsf-1-field-62", time_wait)

    #Check url
    gf.Check_url("https://testingqarvn.com.es/combobox-dependiente/", time_wait)

    #Check message
    gf.Check_text("//p[contains(text(),'Gracias por tu encuesta.')]", 
                  "Gracias", 
                  time_wait
    )