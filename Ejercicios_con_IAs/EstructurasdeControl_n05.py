# @darkgosh Ejercicio proporcionados por IAs
# Practica de Estructuras de control
# 2024-06-21

'''
Sistema de calificaciones

Desarrolla un programa que reciba la calificación de un estudiante en una escala de 0 a 100 y muestre la letra correspondiente a su calificación:

A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59
Utiliza la estructura if-elif-else para determinar la letra correspondiente a la calificación.
'''
#solicita datos
points=int(input("Anota los puntos obtenidos entre 0 a 100 : "))

#Estructura de control
if points >=0 and points <= 59:
    print("Tu clasificacion es : F ")
elif points >=60 and points <= 69:
    print("Tu clasificacion es : D ") 
elif points >=70 and points <= 79:
    print("Tu clasificacion es : C ") 
elif points >=80 and points <= 89:
    print("Tu clasificacion es : B ") 
elif points >=90 and points <= 100:
    print("Tu clasificacion es : A ") 


