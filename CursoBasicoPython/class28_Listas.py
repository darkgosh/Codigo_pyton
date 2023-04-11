"""
Curso Basico de Python
Clase No.28 Uso de listas
@Platzi
@Darkgosh
V1.0
Date: 21/03/2023
"""

def run():
    objetos = ['Hola', 3, 4.5, True, 1]
    for elementos in objetos:
        print(elementos)
    print(objetos[::-1])
    print(objetos[1:3])

    # newElemento = input('Escribre un nuevo elemento: ')
    # newElemento = objetos.append(newElemento)
if __name__ =='__main__':
    run()
