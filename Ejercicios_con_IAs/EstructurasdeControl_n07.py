# @darkgosh Ejercicio proporcionados por IAs
# Practica de Estructuras de control
# Date....

'''
Listado de números pares

Escribe un programa que genere una lista de números pares desde un valor inicial hasta un valor final ingresados por el usuario.

Utiliza un ciclo for para recorrer el rango de números y verificar si cada uno es par
'''
#solicita datos
num_inicial = int(input("Dame el numero inicial: "))
num_final = int(input("Dame el numero final: "))

for i in range(num_inicial,num_final):
    if i % 2 == 0:
        print(i)

'''
def generar_pares(numero_inicial, numero_final):
  """
  Esta función genera una lista de números pares desde un valor inicial hasta un valor final ingresados por el usuario.

  Argumentos:
    numero_inicial (int): El valor inicial del rango.
    numero_final (int): El valor final del rango.

  Retorna:
    list: Una lista que contiene los números pares dentro del rango especificado.
  """
  lista_pares = []
  for numero in range(numero_inicial, numero_final + 1):
    if numero % 2 == 0:
      lista_pares.append(numero)
  return lista_pares

# Solicitar al usuario el valor inicial y final
numero_inicial = int(input("Ingrese el valor inicial: "))
numero_final = int(input("Ingrese el valor final: "))

# Generar la lista de pares
lista_pares_generada = generar_pares(numero_inicial, numero_final)

# Mostrar la lista de pares generada
print("Lista de números pares:", lista_pares_generada)

'''





'''
#Estructura de control
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}", end="\t")
    print()  # Nueva línea después de cada fila

#imprime mensaje
'''
