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
def switch_menu(opcion):
    opciones = {
        'A': 
    }


#Estructura de control


#imprime mensaje

def switch_ejemplo(opcion):
    opciones = {
        'a': "Has elegido la opción A",
        'b': "Has elegido la opción B",
        'c': "Has elegido la opción C"
    }
    return opciones.get(opcion, "Opción no válida")

opcion = input("Elige una opción (a, b, c): ")
print(switch_ejemplo(opcion))