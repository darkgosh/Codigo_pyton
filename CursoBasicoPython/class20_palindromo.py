"""
Curso Basico de Python
Clase No.20 Palindromo 
@Platzi
@Darkgosh
V1.0
Date: 20/03/2023
Nota: Un palindromo es una palabra que se lee igual alderecho y al reves ejemplo: Ana
"""


def palindromo(palabra):
    palabra = palabra.replace(' ', '') #elimina los espacios
    palabra = palabra.lower() #va convertir todas las letras minusculas
    palabra_invertida = palabra[::-1] # va leer la palabra desde el final al principio
    if palabra == palabra_invertida: # compara la palabra con palabra invertida
        return True
    else:
        return False


def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es un Palindromo')
    else:
        print('No es un palindromo')

if __name__ == '__main__':
    run()

