dolares = input ("¿cuantos Dolares tienes?:")
dolares = float(dolares)
valor_mxn = input ("Cuanto vale hoy el peso")
valor_mxn = float(valor_mxn)
pesos = dolares * valor_mxn
pesos = round(pesos, 2)
pesos = str(pesos)
print("Tienes $" + pesos + " Pesos")
# Esta linea solo es para generar cambio en GIT