# @darkgosh Ejercicio proporcionados por https://aprendeconalf.es/
# Practica de Estructuras de control
# Date....

'''
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual 
y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
'''
#solicita datos
inv_inicial = float(input("Ingresa la cantida a Invertir: "))
tasa = int(input("Bloquea la tasa en 1/3/5 Años: \n Para Tasa Anual, Teclea '1' \n Para Tasa a Tres Años, Teclea '3' \n Para Tasa a Cinco Años, Teclea '5' " ))

int_Anual1 = 0.11 / 12
int_Anual3 = 0.13 / 12
int_Anual5 = 0.145 / 12
#Estructura de control
if tasa == 1:
    for i in range(0,tasa * 12):
        inv_inicial += (inv_inicial * int_Anual1)
        print(f"Mes {i+1}: tu Inversion crece a ${round(inv_inicial,2)}")
elif tasa == 3:
    for i in range(0,tasa * 12):
        inv_inicial += (inv_inicial * int_Anual3)
        print(f"Mes {i+1}: tu Inversion crece a ${round(inv_inicial,2)}")
elif tasa == 5:
    for i in range(0,tasa * 12):
        inv_inicial += (inv_inicial * int_Anual5)
        print(f"Mes {i+1}: tu Inversion crece a ${round(inv_inicial,2)}")
else:
    print("Opcion equivocada ")  
          
#imprime mensaje

