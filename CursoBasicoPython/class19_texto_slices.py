"""
Curso Basico de Python
Clase No.19 Texto_Slices
@Platzi
@Darkgosh
V1.0
Date: 20/03/2023
"""

nombre = "francisco"
print(nombre)
print(nombre[0])# indice partiendo de cero muestra la primera letra
print(nombre[1])# indice partiendo de uno muestra la segunda letra
print(nombre[0:3]) # indice partiendo del cero hasta antes del 3
print(nombre[:3]) # indice partiendo del cero hasta antes del 3 // Python lo toma desde cero
print(nombre[3:])# indice partiendo del 3 hasta el ultimo caracter
print(nombre[1:7])# indice partiendo del 1 hasta antes del 7
print(nombre[1:7:2])# indice partiendo del 1 hasta antes del 7 pero en pasos de 2 en 2
print(nombre[::])# indice partiendo del cero hasta el ultimo pero en pasos de 1 en 1
print(nombre[1::3])# indice partiendo del 1 hasta el ultimo pero en pasos de 3 en 3
print(nombre[::-1])# indice partiendo del final hasta el principio retrocediendo de -1 en -1