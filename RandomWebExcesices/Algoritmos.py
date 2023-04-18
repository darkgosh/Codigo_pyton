"""
Curso de Algoritmos y pensamiento Logico
Clase No.18 Metodos con Cadenas de Caracteres.
@Platzi
@Darkgosh
V1.0
Date: 18/04/2023
"""

#ejercicio diagrama de flujo que me de los numeros pares hasta el numero 50

# num = 0
# count = 50

# while count > 0:
#     print(num)
#     num = num + 2
#     count = count - 1

#video juego pokemon pikachu contra jigglypop 

pika_vida = 100
pika_ataque = 55
jiggly_vida = 100
jiggly_ataque = 45
turno = 1

while pika_vida > 0 and jiggly_vida > 0:
    if turno == 1:
        jiggly_vida = jiggly_vida - pika_ataque
        print("Jigglypop tiene todavia " + str(jiggly_vida) + " de vida")
        turno = 0
        print("Termina el Turno de Pikachu ")
    else:
        pika_vida = pika_vida - jiggly_ataque
        print("Pikachu tiene todavia " + str(pika_vida) + " de vida")
        turno = 1
        print("Termina el Turno de Jigglypop ")


