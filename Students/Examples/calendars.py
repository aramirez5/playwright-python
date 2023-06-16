import random
from playwright.sync_api import Playwright
from functions import Global_Functions

#Global variables
time_wait = 0.5
path = "Images/"
url = "https://testingqarvn.com.es/calendarios/"

def test_calendars(playwright: Playwright, url: str = url) -> None:

    #Config
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(
        viewport={"width": 1280, "height": 720}
    )
    page = context.new_page()

    # Go to main page and check title
    page.goto(url)
    gf = Global_Functions(page)
    gf.Check_title("Calendarios | TestingQaRvn", time_wait)
    page.screenshot(path="Images/calendar1.png")

    #Scroll
    gf.Scroll(0, 400, time_wait)
    
    #Wait
    gf.Wait(time_wait)

    #Fill the form
    gf.Text_img("#wsf-1-field-66", "John", path+"calendar2.png", time_wait)
    gf.Text("#wsf-1-field-67", "Doe", time_wait)
    gf.Text("#wsf-1-field-68", "john.doe@gmail.com", time_wait)
    gf.Text("#wsf-1-field-69", "666666666", time_wait)
    gf.Text("#wsf-1-field-70", "Testing Street", time_wait)
    gf.Click("#wsf-1-label-71-row-1", time_wait)
    gf.Click("#wsf-1-label-72-row-1", time_wait)

    #Combobox
    gf.Combo_value("#wsf-1-field-73", "Linux", time_wait)
    num = random.sample(range(1, 4), 1)
    if num[0] == 1:
        gf.Combo_label("#wsf-1-field-75", "Ubuntu", time_wait)
    elif num[0] == 2:
        gf.Combo_label("#wsf-1-field-75", "Debian", time_wait)
    elif num[0] == 3:
        gf.Combo_label("#wsf-1-field-75", "Read Hat", time_wait)

    #Event calendar
    gf.Click("#wsf-1-field-79", time_wait)
    gf.Click("(//div[contains(.,'23')])[9]", time_wait)

    #Calendar
    gf.Text("#wsf-1-field-78", "Junio 22, 2023", time_wait)
    gf.Press_tab_key(time_wait)

    #Submit
    gf.Click("#wsf-1-field-77", time_wait)

    #Check url
    gf.Check_url("https://testingqarvn.com.es/calendarios/", time_wait)

    #Check message
    gf.Check_text(
        "//p[contains(text(),'Gracias por tu encuesta.')]",
          "Gracias", 
          time_wait
    )