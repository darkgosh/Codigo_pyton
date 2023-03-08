def es_primo(numero):  # funcion es_primo que mandare llamar en el programa
    cont = 0  # inicializo contador
    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            cont += 1
    if cont == 0:
        return True
    else:
        return False            

# Esta linea solo es para generar cambio en GIT


def run():
    numero = int(input('Escribe un numero: '))
    if es_primo(numero):
        print('Es primo! ')
    else:
        print('No es primo! ')

if __name__ == '__main__':
    run()
