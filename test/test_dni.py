import pytest
from src.dni import Dni

def test_dni_correcto():
    dni = Dni("12345678Z")
    assert dni.es_letra_correcta() == True

def test_dni_incorrecto():
    dni = Dni("12345678A")
    assert dni.es_letra_correcta() == False