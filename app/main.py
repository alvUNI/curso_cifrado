"""
Este es el archivo principal
"""
## Cifrado Cesar

from funciones.cifrado import cifrado

MENSAJE = "HELLO"
CLAVE = 3

mensaje_cifrado = cifrado(MENSAJE, CLAVE)
print(mensaje_cifrado)
