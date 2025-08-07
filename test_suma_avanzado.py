from suma import suma
import pytest

def test_suma_basicas():
    """Pruebas básicas de suma"""
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0

def test_suma_decimales():
    """Pruebas con números decimales"""
    assert suma(1.5, 2.5) == 4.0
    assert suma(0.1, 0.2) == pytest.approx(0.3)

def test_suma_negativos():
    """Pruebas con números negativos"""
    assert suma(-5, -3) == -8
    assert suma(-10, 15) == 5

def test_suma_grandes():
    """Pruebas con números grandes"""
    assert suma(1000000, 2000000) == 3000000

def test_suma_tipos_invalidos():
    """Pruebas con tipos de datos inválidos"""
    with pytest.raises(TypeError):
        suma("texto", 5)
    with pytest.raises(TypeError):
        suma(None, 5)
