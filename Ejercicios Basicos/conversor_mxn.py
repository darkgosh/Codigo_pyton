pesos = input ("¿cuantos pesos Mexicanos tienes?:")
pesos = float(pesos)
valor_dolar = input ("Cuanto vale hoy el dolar")
valor_dolar = float(valor_dolar)
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dolares")
# Esta linea solo es para generar cambio en GIT