"""
Curso Basico de Python
Clase No.24 For_ recorrer_2
@Platzi
@Darkgosh
V1.0
Date: 20/03/2023
"""


def run():
    nombre = input('Escribe un nombre: ')
    for letra in nombre:
        print(letra)
    
    frase = input(' escribe una frase: ')
    for caracter in frase:
        print(caracter.upper())



    encriptado = list(input ('escribe una contraseña'))
    for Pasw in encriptado:
        print (Pasw + 'aeñk')

if __name__ == '__main__':
    run()