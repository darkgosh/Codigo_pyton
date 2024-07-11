"""
Curso Basico de Python
Clase No.18 Metodos con Cadenas de Caracteres.
@Platzi
@Darkgosh
V1.0
Date: 20/03/2023
"""

nombre = input("¿Cual es tu nombre?:  ")
print(nombre)
print(nombre.upper()) #cambia todas las letras a mayusculas
print(nombre.capitalize()) # Solo cambia la primera letra a Mayusculas
print(nombre.strip()) # quita los espacios
print(nombre.lower()) #cambia todas las letras a Minusculas
print(nombre.replace('o', 'a')) # Cambia las letras ' o ' por letras ' a '
print(nombre[0])# uso de INDICES python devuelve la letra segun la posicion que de coloque entre corchetes [0]
print(len("renato vidana vazquez")) #cuenta el numero de caracteres contenido en el texto. incluyendo los espacios.
