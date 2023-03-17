# contador = 0
# print('2 elevado a '+ str(contador) + ' es igual a: ' + str(2**contador))

# ## programa que combierta MXN a dolares
# pesos_mxn = input("Dime cuantos pesos tienes: ")
# pesos_mxn = float(pesos_mxn)
# valor_dollar2 = 20.19
# dolares2 = pesos_mxn  / valor_dollar2
# dolares2 = str(dolares2)
# print("Tienes  $ "+ dolares2 + " dolares")


## Programa que te entrega la potencia iniciando en cero y limado a la variable LIMITE
# def run():
#     LIMITE = 1024

#     contador = 0 #inicializa contador
#     potencia_2 = 2**contador #crea variable Potencia 
#     while potencia_2 <= LIMITE:
#         print('2 elevado a '+ str(contador) + ' es igual a: ' + str(potencia_2))
#         contador = contador + 1
#         potencia_2 = 2**contador

def run():
    TARGET = 1500
    precio = 1
    while precio <= TARGET:
        print('Precio de  MERCADO:  ' + str(precio))
        precio= precio+1
    print('Posicion abierta: ' + str(precio))


if __name__ == '__main__':
    run()