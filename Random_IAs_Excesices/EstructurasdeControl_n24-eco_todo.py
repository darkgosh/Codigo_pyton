# @darkgosh Ejercicio proporcionados por https://aprendeconalf.es/
# Practica de Estructuras de control
# Date ....

'''
Escribir un programa que muestre el eco de todo lo que el usuario 
introduzca hasta que el usuario escriba “salir” que terminará.
'''
#solicita datos

#Estructura de control
while True:
    print("Hola escribeme algo: ")
    mensaje = input()
    if mensaje != 'Salir':
        print(f"Eco {mensaje} !")
        continue
    if mensaje == 'Salir':
        break
print('Adios')
#imprime mensaje

