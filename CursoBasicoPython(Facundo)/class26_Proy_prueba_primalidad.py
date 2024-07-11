"""
Curso Basico de Python
Clase No.26 Prueba de primalidad
@Platzi
@Darkgosh
V1.0
Date: 21/03/2023
"""
# NOTA: Un numero primimo se define cuando un numero puede dividirse por si mismo y por 1
# https://www.youtube.com/watch?v=e1XtzmR-4jk

def es_primo(numero):  # funcion es_primo que mandare llamar en el programa
    cont = 0  # inicializo contador
    for i in range(1, numero + 1): # se coloca ' numero + 1 ' para incluir el ultimo numero, sino entregara hasta antes del ultimo numero
        if i == 1 or i == numero:# si' i es igual a 1 o i es igual a numero ' ejecuta lo que esta debajo de 'Continue'
            continue
        if numero % i == 0:
            cont += 1
    if cont == 0:
        return True
    else:
        return False            



def run():
    numero = int(input('Escribe un numero: ')) #solicito
    if es_primo(numero): #enuncio funcion es_primo si es true
        print('Es primo! ')
    else:
        print('No es primo! ')

if __name__ == '__main__':
    run()
