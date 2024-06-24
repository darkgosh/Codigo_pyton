# @darkgosh Ejercicio proporcionados por IAs
# Practica de Estructuras de control
# 2024-06-21

'''
Menú de opciones

Diseña un menú de opciones que permita al usuario elegir entre diferentes tareas, como:

Calcular el área de un cuadrado La fórmula para calcular el área de un cuadrado es: area = lado **2 
Calcular el área de un triángulo La fórmula para calcular el área de un triángulo es: (Base * Altura) / 2
Calcular el área de un círculo La fórmula para calcular el área de un círculo es: π x radio **2
Salir
Utiliza la estructura switch (o if-elif-else) para ejecutar la acción 
correspondiente a la opción seleccionada por el usuario.
'''
#solicita datos
opcion = input("Elige una Opcion,Para Calcular el area de: \n Cuadrado 'A'\n Triangulo 'B'\n Circulo 'C'")

#Estructura de control
def switch_menu(opcion): #Estructura de control
    if opcion == 'A':
        lado = float(input("Cuando mide el lado del cuadrado: "))
        calculo = lado**2
        msg = "El area del cuadrado es:" 
        return  msg , calculo
    elif opcion == 'B':
        base = float(input("Cuando mide la base: "))
        altura = float(input("Cuando mide el altura: "))
        calculo = (base * altura) / 2
        msg = "El area del Triangulo es:" 
        return  msg , calculo
    elif opcion == 'C':
        radio = float(input("Cuando mide el radio: "))
        pi = 3.1416
        calculo = (pi * radio) **2
        msg = "El area del Circulo es:" 
        return  msg , calculo
    else:
        return "Opción no válida"
    

print(switch_menu(opcion))  # Imprime Opcion deseada


#imprime mensaje

'''
opcion = input("Elige una Opcion,Para Calcular el area de: \n Cuadrado 'a'\n Triangulo 'b'\n Circulo 'c'")

def switch_ejemplo(opcion):
    if opcion == 'a':
        return "Has elegido la opción A"
    elif opcion == 'b':
        return "Has elegido la opción B"
    elif opcion == 'c':
        return "Has elegido la opción C"
    else:
        return "Opción no válida"

print(switch_ejemplo(opcion))  # Imprime: Has elegido la opción C
'''