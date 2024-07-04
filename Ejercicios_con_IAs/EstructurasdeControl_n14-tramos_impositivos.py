# @darkgosh Ejercicio proporcionados por https://aprendeconalf.es/
# Practica de Estructuras de control
# Date 20240703

'''
Los tramos impositivos para la declaración de la renta 
en un determinado país son los siguientes:

Renta	Tipo impositivo
Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	45%
Escribir un programa que pregunte al usuario su renta anual 
y muestre por pantalla el tipo impositivo que le corresponde.
'''
#solicita datos
rent_anual = int(input("Cuanto fue tu ingreso anual? "))
#Estructura de control
if rent_anual > 60000:
        print("Ganas un chingo asi que, ")
        tax = rent_anual * 0.45
        print(f"te vamos a ensartar: con ${tax} de Impuestos")
elif rent_anual > 35000 and rent_anual < 60000 :
        print("Ganas Bastante asi que, ")
        tax = rent_anual * 0.30
        print(f"caite con: ${tax} de Impuestos")
elif rent_anual > 20000 and rent_anual < 35000 :
        print("Ganas masomenos asi que, ")
        tax = rent_anual * 0.20
        print(f"debes pagar: ${tax} de Impuestos")
elif rent_anual > 10000 and rent_anual < 20000 :
        print("Ganas poco aun asi, ")
        tax = rent_anual * 0.15
        print(f"debes pagar: ${tax} de Impuestos")        
else:
        print("Ganas una madre pero de todos modos, ")
        tax = rent_anual * 0.05
        print(f"afloja: ${tax} de Impuestos")



