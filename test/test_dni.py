import pytest
from src.dni import Dni
import random

def test_obtener_dni():
    cadena = "78484464T"
    dni = Dni(cadena)
    assert cadena == dni.obtener_dni()
    
def test_comprobar_numero():
    cadena = "78484464T"
    dni = Dni(cadena)
    assert True == dni.comprobar_numero()
    
def test_comprobar_letra():
    cadena = "78484464T"
    dni = Dni(cadena)
    assert True == dni.comprobar_letra()
    
def test_comprobar_dni():
    cadena = "78484464T"
    dni = Dni(cadena)
    assert True == dni.comprobar_dni()
    
def test_validar_dni():
    cadena = "78484464T"
    dni = Dni(cadena)
    assert True == dni.validar_dni()

def generar_dnis_random():
    return [
        str(random.randint(10000000, 99999999)) + random.choice("TRWAGMYFPDXBNJZSQVHLCKE")
        for _ in range(10)
    ]
def test_dnis_random(): # Para que funcione este test, realizar el pytest -s 

    dnis = generar_dnis_random()

    for cadena in dnis:
        dni = Dni(cadena)

        if dni.validar_dni():
            print(f"El DNI {cadena} es válido.")
        else:
            print(f"El DNI {cadena} no es válido.")
