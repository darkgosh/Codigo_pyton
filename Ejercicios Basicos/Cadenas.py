# Ejercicio 8
# # Escribir un programa que pida al usuario un número entero y 
# # muestre por pantalla un triángulo rectángulo como el de más abajo.
# num = int(input('Dame un numero al azar: '))
# for i in range(num):
#     for j in range( i + 1 ):
#         print(' @ ', end='')
#     print('')

# Esta linea solo es para generar cambio en GIT

# Ejercicio 5
# Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, y muestre por pantalla el capital 
# obtenido en la inversión cada año que dura la inversión.

inv = int(input('Cuanto dinero vas a invertir? '))
int_anual =int(input('Dame la Tasa anual esperada: '))
anios = int(input('Dame el periodo en años: '))
porcent = int_anual/100
roi_anual = (inv * porcent) / 12
print('El interes mensual equivale a: '+ str(roi_anual))
for i in range(anios):
    roi_anual = inv + porcent
    i+1
    print(str(roi_anual))
