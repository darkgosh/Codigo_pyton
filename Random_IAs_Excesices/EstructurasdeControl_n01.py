# @darkgosh Ejercicio proporcionados por IAs
# Practica de Estructuras de control
# 2024-06-10

'''
Escribe un programa que solicite al usuario un número entero 
y lo clasifique como positivo, negativo o cero.
'''
num = int(input(f"Dame un numero"))

if num > 0:
    print(f"El numero {num} es positivo ")
elif num == 0:
    print(f"El numero {num} es igual a cero")
else:
    print(f"El numero {num} es Negativo")