"""
Curso Basico de Python
Clase No.24 For_ recorrer
@Platzi
@Darkgosh
V1.0
Date: 20/03/2023
"""

def run():
    nombre = input('Escribe tu nombre: ')
    for letra in nombre:
        print(letra)
    frase = input('Escribe una frase: ')
    for caracter in frase:
        print(caracter.upper())


if __name__ == '__main__':
    run()
