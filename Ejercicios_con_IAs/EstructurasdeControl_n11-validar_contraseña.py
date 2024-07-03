# @darkgosh Ejercicio proporcionados por https://aprendeconalf.es/
# Practica de Estructuras de control
# 2024-06-21

'''
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
por el usuario coincide con la guardada en la variable 
sin tener en cuenta mayúsculas y minúsculas.
'''
#solicita datos
con = input("Hola dame la contrasenia de acceso: ")
PASSWORD = "reNato"
#Estructura de control
if con.lower() == PASSWORD.lower():
    print("Acceso concedido: ")
else:
    print("Incorrecct password !!")
#imprime mensaje

