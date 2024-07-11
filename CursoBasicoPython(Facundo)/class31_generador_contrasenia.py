"""
Curso Basico de Python
Clase No.31 Generador de contrasenias
@Platzi
@Darkgosh
V1.0
Date: 21/03/2023
"""
import random
def generar_contrasena():
    mayusculas = ['A','B', 'C', 'D','E','F','G']
    minusculas = ['a','b','c','d','e','f','g']
    simbolos = ['!','#','$','&','/','(',')']
    numeros = ['1','2','3','4','5','6','7','8','9','0']

    caracteres = mayusculas + minusculas + simbolos + numeros
    contrasenia = []
    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasenia.append(caracter_random)
    contrasenia = "".join(contrasenia)
    return contrasenia

def run():
    contrasena = generar_contrasena()
    print('Tu nueva contrasenia es: ' + contrasena)
if __name__ =='__main__':
    run()
