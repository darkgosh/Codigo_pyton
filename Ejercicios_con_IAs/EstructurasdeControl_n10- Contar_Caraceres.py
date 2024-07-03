# @darkgosh Ejercicio proporcionados por IAs
# Practica de Estructuras de control
# Date....

'''
Análisis de texto

Escribe un programa que lea un texto ingresado por el usuario 
y cuente la cantidad de letras, dígitos y espacios en blanco que contiene.

Utiliza un ciclo for para recorrer cada carácter del texto y verificar su tipo 
(letra, dígito o espacio).

tambien agregar si es minuscula o es mayuscula caracter.isupper() y caracter.islower().
Estos ejercicios te ayudarán a practicar el uso de diferentes estructuras de control en Python, 
como if-elif-else, while, for y switch, para controlar el flujo de ejecución de tu código y realizar tareas diversas.
'''
#solicita datos
def contar_caracteres(texto):
  """
  Esta función cuenta la cantidad de letras, dígitos y espacios en blanco en un texto ingresado por el usuario.

  Argumentos:
    texto (str): El texto que se desea analizar.

  Retorna:
    dict: Un diccionario con las siguientes claves:
      "letras": Cantidad de letras en el texto.
      "digitos": Cantidad de dígitos en el texto.
      "espacios": Cantidad de espacios en blanco en el texto.
  """
  conteo_caracteres = {"letras": 0, "digitos": 0, "espacios": 0, "mayusculas":0, "minusculas":0}

  for caracter in texto:
    if caracter.isalpha():
      conteo_caracteres["letras"] += 1
      if caracter.isupper():
        conteo_caracteres["mayusculas"] += 1
      else:
        conteo_caracteres["minusculas"] += 1
    elif caracter.isdigit():
      conteo_caracteres["digitos"] += 1
    else:
      conteo_caracteres["espacios"] += 1

  return conteo_caracteres

# Solicitar al usuario el texto
texto_usuario = input("Ingrese un texto: ")

# Contar los caracteres
conteo_caracteres = contar_caracteres(texto_usuario)

# Mostrar el conteo de caracteres
print("Cantidad de letras:", conteo_caracteres["letras"])
print("Cantidad de dígitos:", conteo_caracteres["digitos"])
print("Cantidad de espacios:", conteo_caracteres["espacios"])
print("Cantidad de Minusculas:", conteo_caracteres["minusculas"])
print("Cantidad de Mausculas:", conteo_caracteres["mayusculas"])
#Estructura de control



#imprime mensaje

