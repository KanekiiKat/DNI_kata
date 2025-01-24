import pytest
from src.dni import Dni
from src.asignador_caracter import AsignadorCaracter

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