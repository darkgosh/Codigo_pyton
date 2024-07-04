# @darkgosh Ejercicio proporcionados por https://aprendeconalf.es/
# Practica de Estructuras de control
# Date....

'''
Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
'''
#solicita datos
num = int(input("Dame un numero entero"))

#Estructura de control
for i in range(num):
    cosiente = num % 2
    if cosiente !=0:
        print ("Numeros impares {cosiente}")
    


#imprime mensaje

