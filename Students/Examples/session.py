from functions import Global_Functions
from config_test import set_up_demo, set_up_session_username, set_up_session_password

# Global variables
time_wait = 0.5
path = "Images/"
pdf = "C:/laragon/www/playwright-python/Students/Examples/Documents/sample.pdf"

def test_session_one(set_up_demo) -> None:
    
    page = set_up_demo  # ruff: noqa
    gf = Global_Functions(page)
    gf.Check_title("Swag Labs", time_wait)

def test_session_two(set_up_demo) -> None:
    
    page = set_up_demo  # ruff: noqa
    gf = Global_Functions(page)

    gf.Click("#add-to-cart-sauce-labs-backpack", time_wait)
    gf.Click("#add-to-cart-sauce-labs-bike-light", time_wait)
    gf.Wait(time_wait)

def test_session_three(set_up_demo) -> None:
    
    page = set_up_demo  # ruff: noqa
    gf = Global_Functions(page)

    gf.Click("#react-burger-menu-btn", time_wait)
    gf.Click("#reset_sidebar_link", time_wait)
    gf.Click("#react-burger-cross-btn", time_wait)
    
    gf.Wait(time_wait)

def test_session_four(set_up_demo) -> None:
    
    page = set_up_demo  # ruff: noqa
    gf = Global_Functions(page)

    gf.Click("#remove-sauce-labs-backpack", time_wait)
    gf.Click("#remove-sauce-labs-bike-light", time_wait)
    gf.Click("#react-burger-menu-btn", time_wait)
    gf.Click("#logout_sidebar_link", time_wait)
    
    gf.Wait(time_wait)

def test_username(set_up_session_username) -> None:
    
    page = set_up_session_username  # ruff: noqa
    gf = Global_Functions(page)

    error_message = gf.Get_text("//h3[contains(@data-test,'error')]", time_wait)
    expected_message = "Epic sadface: Username and password do not match any user in this service"
    assert error_message in expected_message, "The error message is not correct"
    
    gf.Wait(time_wait)

def test_password(set_up_session_password) -> None:
    
    page = set_up_session_password  # ruff: noqa
    gf = Global_Functions(page)

    error_message = gf.Get_text("//h3[contains(@data-test,'error')]", time_wait)
    expected_message = "Epic sadface: Username and password do not match any user in this service"
    assert error_message in expected_message, "The error message is not correct"

    gf.Wait(time_wait)