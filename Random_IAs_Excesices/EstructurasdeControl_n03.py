# @darkgosh Ejercicio proporcionados por IAs
# Practica de Estructuras de control
# 2024-06-10

'''
 Año bisiesto

Crea un programa que determine si un año ingresado por el usuario es bisiesto o no. Un año es bisiesto si es divisible por 4, pero no por 100, a menos que también sea divisible por 400.

Utiliza la estructura if anidada para verificar las condiciones de año bisiesto.
'''
anio = int(input("Ingrese un año: "))

if (anio % 4 == 0) and (anio % 100 != 0) or anio % 400 == 0:
  print(f"El año {anio} es bisiesto.")
else:
  print(f"El año {anio} no es bisiesto.")
