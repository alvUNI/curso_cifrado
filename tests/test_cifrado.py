"""
    Este modulo es para hacer un test
"""
import pytest
from app.funciones.cifrado import cifrado

@pytest.mark.parametrize(
        "mensaje,clave,expected_result",
        [("HELLO",3,"KHÑÑS"),
        ("PYTHON",5,"VDYMUS"),
        ("WORLD",1,"XPSME")]
)
def test_cifrado(mensaje,clave,expected_result):
    """
        Test para el cifrado
    """
    assert cifrado(mensaje, clave) == expected_result
