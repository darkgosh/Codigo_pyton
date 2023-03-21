"""
Curso Basico de Python
Clase No.29 Uso de tuplas
@Platzi
@Darkgosh
V1.0
Date: 21/03/2023
"""

def run():
    numeros = [1, 2 ,3, 4, 5]
    print(numeros)
    numeros.append('Hola')
    print(numeros)
    numeros.pop(5)
    print(numeros)
    numeros2 = [6,7,8,9,10]
    listaFinal = numeros + numeros2
    print(listaFinal)
    numeros = [1, 2 ,3, 4, 5] * 5
    print(numeros)
    print('            ')
    mi_tupla = (1,2,3,4,5)
    print(mi_tupla)
    for numero in mi_tupla:
        print(numero)

if __name__ =='__main__':
    run()
