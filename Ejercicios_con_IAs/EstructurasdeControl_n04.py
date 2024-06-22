# @darkgosh Ejercicio proporcionados por IAs
# Practica de Estructuras de control
# Date....

'''
Clasificación de edades
Escribe un programa que solicite al usuario su edad y muestre un mensaje en función del rango de edad:
Niño: menor de 12 años
Adolescente: entre 12 y 18 años
Adulto: entre 18 y 65 años
Adulto mayor: mayor de 65 años
Utiliza la estructura if-elif-else para clasificar la edad del usuario.
'''
#solicita datos
edad= int(input("Escribe tu edad: "))

#estructura de control
if edad <= 12:
  print(f"Con {edad} años, Eres un Niño" )
elif edad > 12 and edad <=17:
  print(f"Con {edad} años, Eres un Adolesente" )
else:
  print(f"Con {edad} años, Eres un Adulto" )

