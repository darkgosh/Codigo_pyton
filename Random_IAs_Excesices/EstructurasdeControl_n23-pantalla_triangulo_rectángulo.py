# @darkgosh Ejercicio proporcionados por https://aprendeconalf.es/
# Practica de Estructuras de control
# Date 20240709

'''
Escribir un programa que pida al usuario un número entero 
y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
*
**
***
****
*****
'''
#solicita datos
tree = int(input("Dame un numero entero: "))
icono = "*"
#Estructura de control
for i in range(0,tree):
    print(i*icono)


#imprime mensaje

