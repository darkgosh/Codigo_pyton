# @darkgosh Ejercicio proporcionados por IAs
# Practica de Estructuras de control
# Date....

'''
Patrones de asteriscos

Crea un programa que imprima patrones de asteriscos en forma de pirámide, triángulo invertido, diamante, etc., 
según la altura o número de filas que ingrese el usuario.

Utiliza ciclos for anidados para controlar la posición de los asteriscos en cada fila y columna.
'''
#solicita datos
n = int(input("Dame un numero entero: "))

for i in range (n):
    for j in range(i+1):
        print("^", end="")
    print("")
#Estructura de control


#imprime mensaje

