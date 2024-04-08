"""
La fucnion principal cifrado
"""

LETRAS = "ABCDEFGHIJKLMNÑOPRSTUVWXYZ"

def cifrado(mensaje, clave):
    """
    Cifra un mensaje utilizando el cifrado de César.

    Args:
        mensaje (str): El mensaje a cifrar.
        clave (int): La clave de cifrado.

    Returns:
        str: El mensaje cifrado.

    """
    mensaje_cifrado = ""
    for letra in mensaje.upper():
        if letra in LETRAS:
            posicion = LETRAS.index(letra)
            nueva_posicion = (posicion + clave)%len(LETRAS)
            mensaje_cifrado += LETRAS[nueva_posicion]
        else:
            mensaje_cifrado += letra
    return mensaje_cifrado
