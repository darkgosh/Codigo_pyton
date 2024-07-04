# @darkgosh Ejercicio proporcionados por https://aprendeconalf.es/
# Practica de Estructuras de control
# Date 20240703

'''
Para tributar un determinado impuesto se debe ser mayor de 16 años 
y tener unos ingresos iguales o superiores a 1000 € mensuales. 
Escribir un programa que pregunte al usuario su edad 
y sus ingresos mensuales 
y muestre por pantalla si el usuario tiene que tributar o no.
'''
#solicita datos
edad = int(input("¿Cual es tu edad? "))
sueldo = int(input("¿Cual es tu sueldo Mensual? "))


#Estructura de control
if edad > 16 and sueldo >= 1000:
        print("Eres mayor de edad y ")
        tax = sueldo * 0.16
        print(f"Debes pagar: ${tax} de Impuestos")
else:
        print("No te toca pagar impuestos")
    
#imprime mensaje
