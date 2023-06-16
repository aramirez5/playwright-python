import pytest
from functions import Global_Functions
from config_test import set_up_parametrized

# Global variables
time_wait = 0.5
path = "Images/"
pdf = "C:/laragon/www/playwright-python/Students/Examples/Documents/sample.pdf"
data = [("Rodrigo", "Villanueva"),("Juan", "Pérez"), ("Erika", "Paz")]
data2 = {
    'argnames': 'nom, ape',
    'argvalues': [("Rodrigo", "Villanueva"),("Juan", "Pérez"), ("Erika", "Paz")]
} 

@pytest.mark.parametrize("nom, ape",[("Rodrigo", "Villanueva"),("Juan", "Pérez"), ("Erika", "Paz")])
def test_parametrized_one(set_up_parametrized, nom, ape) -> None:
    
    page = set_up_parametrized  # ruff: noqa
    gf = Global_Functions(page)

    gf.Check_title("Datos Personales | TestingQaRvn", time_wait)

    gf.Text("//input[@id='wsf-1-field-21']", nom, time_wait)
    gf.Text("//input[@id='wsf-1-field-22']", ape, time_wait)
    gf.Wait(time_wait)

@pytest.mark.parametrize("nom, ape", data)
def test_parametrized_two(set_up_parametrized, nom, ape) -> None:
    
    page = set_up_parametrized  # ruff: noqa
    gf = Global_Functions(page)

    gf.Check_title("Datos Personales | TestingQaRvn", time_wait)

    gf.Text("//input[@id='wsf-1-field-21']", nom, time_wait)
    gf.Text("//input[@id='wsf-1-field-22']", ape, time_wait)
    gf.Wait(time_wait)

@pytest.mark.parametrize(**data2)
def test_parametrized_two(set_up_parametrized, nom, ape) -> None:
    
    page = set_up_parametrized  # ruff: noqa
    gf = Global_Functions(page)

    gf.Check_title("Datos Personales | TestingQaRvn", time_wait)

    gf.Text("//input[@id='wsf-1-field-21']", nom, time_wait)
    gf.Text("//input[@id='wsf-1-field-22']", ape, time_wait)
    gf.Wait(time_wait)