"""
Curso Basico de Python
Clase No.21 y 22 Bucles While
@Platzi
@Darkgosh
V1.0
Date: 20/03/2023
Problema: Imprime todos las potencias de 2 hasta llegar al numero 1024
"""

#class 21 ejemplo de como hacerlo manual sin un bucle
# contador = 0
# print('2 elevado a '+ str(contador) + ' es igual a: ' + str(2**contador)) 
# contador = 1
# print('2 elevado a '+ str(contador) + ' es igual a: ' + str(2**contador))
# contador = 2
# print('2 elevado a '+ str(contador) + ' es igual a: ' + str(2**contador))


# Class 22 ciclo while
def run():
    LIMITE = 1024 #Constante va en mayusculas

    contador = 0
    potencia_2 = 2**contador
    while potencia_2 <= LIMITE:
        print('2 elevado a '+ str(contador) + ' es igual a: ' + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador


if __name__ == '__main__':
    run()