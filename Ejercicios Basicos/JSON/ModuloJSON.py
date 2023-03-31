# Importar el módulo
import json
import os

directorio = os.getcwd()
directorio_actual = directorio + "\Ejercicios Basicos\JSON"
print("El directorio Actual es: ",directorio_actual)

# json.<funcion>(<args>) Sintaxis para llamar la funcion definida en el modul json

# Cadena de caracteres en el formato JSON
datos_JSON =  """
{
	"tamano": "mediana",
	"precio": 15.67,
	"toppings": ["champinones", "queso extra", "pepperoni", "albahaca"],
	"cliente": {
		"nombre": "Jane Doe",
		"telefono": "455-344-234",
		"correo": "janedoe@email.com"
	}
}
"""

#Para hacerlo, usaremos la función loads() del módulo json, pasando la cadena de caracteres como argumento.
#json.loads(<cadena_json>)

datos_diccionario = json.loads(datos_JSON)
#print(datos_diccionario)
print(datos_diccionario["tamano"])
print(datos_diccionario["precio"])
print(datos_diccionario["toppings"])
print(datos_diccionario["cliente"])


""" crear una cadena de caracteres en formato JSON a partir de un objeto (por ejemplo, 
    un diccionario) para mostrarla, guardarla, o usarla como una cadena de caracteres en el programa.
    Para hacerlo, puedes usar la función dumps del módulo json, pasando el objeto como argumento 
"""
# json.dump(<Objeto>)


# Diccionario Python
cliente = {
    "nombre": "Nora",
    "edad": 56,
    "id": "45355",
    "color_ojos": "verdes",
    "usa_lentes": False
}

'''
    json.dumps(cliente) crea y retorna una cadena de caracteres con todos los pares clave-valor del diccionario en formato JSON.
'''
# Obtener una cadena de caracteres JSON
cliente_JSON1 = json.dumps(cliente,indent=2)
cliente_JSON = json.dumps(cliente,indent=2,sort_keys=True)

print("\n",cliente_JSON1,"\n")
print("\n",cliente_JSON,"\n")

with open(directorio_actual + "\ordenes.json") as archivo:
    datos = json.load(archivo)
    print("\n",datos,"\n")
    print(len(datos["ordenes"]),"\n") #El resultado es 2 porque el valor de la clave principal "orders" es una lista con dos elementos.
    print(datos["ordenes"][0]["toppings"],"\n")


# Abrir el archivo ordenes.json
with open(directorio_actual + "\ordenes.json") as archivo:
    # Cargar su contenido y crear un diccionario
    datos = json.load(archivo)

    # Eliminar el par clave-valor "cliente" de cada orden
    for orden in datos["ordenes"]:
        del orden["cliente"]

# Abrir (o crear) un archivo ordenes_nuevo.json 
# y guardar la nueva versión de la información
with open(directorio_actual + "\ordenes_nuevo.json", 'w') as archivo_nuevo:
    json.dump(datos, archivo_nuevo,indent=4)


# load() VS loads()
"""
Dato: Piensa en loads() como "load string" (cargar cadena de caracteres). 
Esto te ayudará a identificar la función que se usa para cada propósito.
"""


# dump() VS dumps()
"""
Dato: Piensa en dumps() como "dump string" (dump cadena de caracteres) 
y esto te ayudará a identificar la función que se usa para cada propósito.
"""