# @darkgosh Ejercicio proporcionados por https://aprendeconalf.es/
# Practica de Estructuras de control
# Date....

'''
Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
'''
#solicita datos

num = int(input("Dame un numero entero positivo: "))

#Estructura de control
for i in range(num,-1,-1):
    print(f"{i}", end=", ")


#imprime mensaje

