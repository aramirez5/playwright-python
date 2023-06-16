import random
from playwright.sync_api import Playwright
from functions import Global_Functions

#Global variables
time_wait = 0.5
path = "Images/"
pdf = "C:/laragon/www/playwright-python/Students/Examples/Documents/sample.pdf"
url = "https://testingqarvn.com.es/upload-files/"

def test_upload(playwright: Playwright, url: str = url) -> None:

    #Config
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(
        viewport={"width": 1280, "height": 720}
    )

    #Trace viewer start
    #context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()

    # Go to main page and check title
    page.goto(url)
    gf = Global_Functions(page)
    gf.Check_title("Upload Files | TestingQaRvn", time_wait)
    page.screenshot(path="Images/upload1.png")

    #Scroll
    gf.Scroll(0, 400, time_wait)
    
    #Wait
    gf.Wait(time_wait)

    #Fill the form
    gf.Text_img("#wsf-1-field-80", "John", path+"upload2.png", time_wait)
    gf.Text("#wsf-1-field-81", "Doe", time_wait)
    gf.Text("#wsf-1-field-82", "john.doe@gmail.com", time_wait)
    gf.Text("#wsf-1-field-83", "666666666", time_wait)
    gf.Text("#wsf-1-field-84", "Testing Street", time_wait)
    gf.Click("#wsf-1-label-85-row-1", time_wait)
    gf.Click("#wsf-1-label-86-row-1", time_wait)

    #Combobox
    gf.Combo_value("#wsf-1-field-87", "Linux", time_wait)
    num = random.sample(range(1, 4), 1)
    if num[0] == 1:
        gf.Combo_label("#wsf-1-field-89", "Ubuntu", time_wait)
    elif num[0] == 2:
        gf.Combo_label("#wsf-1-field-89", "Debian", time_wait)
    elif num[0] == 3:
        gf.Combo_label("#wsf-1-field-89", "Read Hat", time_wait)

    #Event calendar
    gf.Click("#wsf-1-field-91", time_wait)
    gf.Click("(//div[contains(.,'23')])[9]", time_wait)

    #Calendar
    gf.Text("#wsf-1-field-92", "Junio 22, 2023", time_wait)
    gf.Press_tab_key(time_wait)

    #Upload file
    gf.Upload_file("#wsf-1-field-94", pdf, time_wait)

    #Remove file
    gf.Upload_file_remove("#wsf-1-field-94", time_wait)

    #Upload file again
    gf.Upload_file("#wsf-1-field-94", pdf, time_wait)

    #Submit
    gf.Click("#wsf-1-field-93", time_wait)

    #Check url
    gf.Check_url("https://testingqarvn.com.es/upload-files/", time_wait)

    #Check message
    gf.Check_text("//p[contains(text(),'Gracias por tu encuesta.')]", 
                  "Gracias", 
                  time_wait
    )

    #Trace viewer stop
    #context.tracing.stop(path="trace.zip")