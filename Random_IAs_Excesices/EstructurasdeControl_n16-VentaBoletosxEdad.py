# @darkgosh Ejercicio proporcionados por https://aprendeconalf.es/
# Practica de Estructuras de control
# Date 20240704

'''
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática 
el precio que debe cobrar a sus clientes por entrar. 
El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
Si el cliente es menor de 4 años puede entrar gratis, 
si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

'''
#solicita datos
edad = int(input("Cual es tu edad? : "))

#Estructura de control
if edad <= 4:
    print("Eres menor de edad puedes pasar gratis!!! ")
elif edad >4 and edad <18:    
    print("Eres un Niño, deber pagar 5 dolares  !!! ")
elif edad >=18 and edad < 70:    
    print("Eres un adulto, deber pagar 10 dolares  !!! ")
else:
    print("Eres una persona mayor,por tu seguridad No puedes pasar  !!! ")



