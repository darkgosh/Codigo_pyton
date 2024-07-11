# @darkgosh Ejercicio proporcionados por https://aprendeconalf.es/
# Practica de Estructuras de control
# Date 20240703

'''
Los alumnos de un curso se han dividido en dos grupos A y B 
de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior 
a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. 
Escribir un programa que pregunte al usuario su nombre y sexo, 
y muestre por pantalla el grupo que le corresponde.
'''

#solicita datos

name_user = input("¿Cual es tu nombre?: ")
gender_user = input("¿Cual es tu sexo (H/M)?: ").upper()

#Funcion
def asignar_grupo(name,gender):
   name_mayusculas = name.upper()
   if gender == "M" and name_mayusculas[0] <"M":
      grupo="A"
   elif gender == "H" and name_mayusculas[0] >"N":
      grupo="A"
   else:
    grupo ="B"
   return grupo

user_group = asignar_grupo(name_user,gender_user)
#imprime mensaje
print(f"Perteneces al grupo {user_group}")
