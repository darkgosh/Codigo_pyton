# @darkgosh Ejercicio proporcionados por https://aprendeconalf.es/
# Practica de Estructuras de control
# Date 20240709

'''
Escribir un programa que pida al usuario un número entero 
y muestre por pantalla un triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
'''

#solicita datos
numero = int(input("Ingrese un número entero para crear el triángulo: "))
for fila in range(1, numero + 1):
    for columna in range(1, fila + 1):
      print(f"{columna}", end=" ")
    print()
'''

#Estructura de control
numero_maximo = int(input("Ingrese un número entero para crear el triángulo: "))
for fila in range(0, numero_maximo + 1):
    # Imprimir números en la fila actual
    for numero in range(0, fila + 1):
      print(numero, end=" ")
    # Salto de línea para pasar a la siguiente fila
    print()

#imprime mensaje

'''