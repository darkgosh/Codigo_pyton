"""
Curso Basico de Python
Clase No.27 Videojuego
@Platzi
@Darkgosh
V1.0
Date: 21/03/2023
"""
# objetivo del juego adivina un numero de 0-100
# uso de modulos de pythom
import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elieje un numero al azar: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Elige un numero mas grande")
        else:
            print('Elige un numero mas chico')
        numero_elegido = int(input("Vuelve a elegir un numero: "))
    print("! Ganaste !")



if __name__ =='__main__':
    run()
