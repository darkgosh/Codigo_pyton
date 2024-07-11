# @darkgosh Ejercicio proporcionados por IAs
# Practica de Estructuras de control
# Date....

'''
Tablas de multiplicar

Imprime una tabla de multiplicar de un número ingresado por el usuario, desde el 1 hasta un factor de multiplicación también especificado por el usuario.

Utiliza dos ciclos for anidados, uno para recorrer los números de la tabla y otro para los factores de multiplicación.
'''
#solicita datos
table = int(input("Dame la numero dela tabla: "))


#Estructura de control
for i in range(table,table+1):
    for j in range (1,11):
        print(f"{i} x {j} = {i * j}")    #imprime mensaje




'''

for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}", end="\t")
    print()  # Nueva línea después de cada fila


'''
