from ast import Str

''' 
##programa que combierta Pesos Colombianos a dolares
# Esta linea solo es para generar cambio en GIT
pesos = input("Cuantos pesos colombianos tienes: ")
pesos = float(pesos)
valor_dollar = 3875
dolares = pesos / valor_dollar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dolares") 

## programa que combierta MXN a dolares

pesos_mxn = input("Dime cuantos pesos tienes: ")
pesos_mxn = float(pesos_mxn)
valor_dollar2 = 20.19
dolares2 = pesos_mxn  / valor_dollar2
dolares2 = Str(dolares2)
print("Tienes  $ "+ dolares2 + " dolares")
'''
def conversor(tipo_pesos, valor_dolar):
    pesos = input('Cuantos pesos '+ tipo_pesos + ' tienes: ')
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares") 

menu = """
Bienvenido al coversor de monedas $

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una Opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor('Colombianos', 3875)
    
elif opcion == 2:
    conversor('Argentinos', 65)

elif opcion == 3:
   conversor('Mexicanos', 20.19)

else:
    print('Ingresa una opcion correcta por favor')

