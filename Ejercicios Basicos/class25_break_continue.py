"""
Curso Basico de Python
Clase No.25 Break and Continue
@Platzi
@Darkgosh
V1.0
Date: 21/03/2023
"""

def run():
    # for contador in range (1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break

    # texto = input('Escribe un texto: ')
    # for letra in texto:
    #     if letra == 'o':
    #         break
    #     if letra == 'O':
    #         break
    #     print(letra)

    # contador = 1
    # print(contador)
    # while contador < 100:
    #     contador = contador +1
    #     if contador == 51:
    #         break
    #     print(contador)

    contador = 1
    print(contador)
    while contador < 100:
        contador = contador +1
        if contador % 2 != 0:
            break
        print(contador)


if __name__ == '__main__':
    run()