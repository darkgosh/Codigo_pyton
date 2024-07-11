# @darkgosh Ejercicio proporcionados por IAs
# Practica de Estructuras de control
# 2024-06-10

'''
Crea una calculadora simple que permita al usuario realizar 
operaciones básicas como suma, resta, multiplicación y división
'''

op = input("Ingrese el operador deseado (+, -, *, /): ")
print(op)

num1 = float(input("Dame el primer numero: "))
num2 = float(input("Dame el primer segundo: "))

if op == "+":
    resultado = num1 + num2
    print("El resultado de la Suma es: ")
    print(resultado)
elif op == "-":
    resultado = num1 - num2
    print("El resultado de la Resta es: ")
    print(resultado)
elif op == "*":
    resultado = num1 * num2
    print("El resultado de la Resta es: ")
    print(resultado)
elif op == "/":
  if num2 != 0:
    resultado = num1 / num2
    print("El resultado de la Resta es: ")
    print(resultado)
  else:
     print("no se puede dividir entre cero")
else:
   print("El operador no es valido")

  
