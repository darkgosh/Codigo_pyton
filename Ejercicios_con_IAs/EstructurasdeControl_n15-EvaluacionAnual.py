# @darkgosh Ejercicio proporcionados por https://aprendeconalf.es/
# Practica de Estructuras de control
# Date 20240703

'''
En una determinada empresa, sus empleados son evaluados al final de cada año. 
Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, 
traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados 
pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. 
A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. 
La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel	Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, 
así como la cantidad de dinero que recibirá el usuario.
'''

#Estructura de control
empleados = ["Renato", "Manuel", "Adán", "Fernando", "Helenita", "Nubis"]  

calificaciones = []  # Lista para almacenar las calificaciones
note = [] # Lista para almacenar las las notas deacuerdo a su bono
for empleado in empleados:
    calificacion = input(f"Ingrese la calificación de {empleado} (I/A/M): ").upper()  # Convertir la entrada a mayúsculas
    while calificacion not in ["I", "A", "M"]:  # Validar la entrada
        calificacion = input("Calificación no válida. Ingrese I, A o M: ").upper()
    calificaciones.append(calificacion)  # Metodo .append para almacenar la calificación en la lista calificaciones

# Ordenar las calificaciones
calificaciones_ordenadas = []
for calificacion in calificaciones:
    if calificacion == "M":
        calificaciones_ordenadas.append(calificacion)
        bono = (0.6 * 2400)
        note.append(f"Tu desempeño fue Meritorio, Ganaste un bono de ${bono}")
for calificacion in calificaciones:
    if calificacion == "A":
        calificaciones_ordenadas.append(calificacion)
        bono = (0.4 * 2400)
        note.append(f"Tu desempeño fue Aceptable, Ganaste un bono de ${bono}")
for calificacion in calificaciones:
    if calificacion == "I":
        calificaciones_ordenadas.append(calificacion)
        bono = (0.0)
        note.append(f"Tu desempeño fue Inaceptable, No amerita bono")

# Imprimir las calificaciones ordenadas del mejor al peor
print("Calificaciones ordenadas:")
for i, empleado in enumerate(empleados):
    print(f"{i + 1}. {empleado}: Tu calificacion es: {calificaciones_ordenadas[i]}\n Esto quiere decir que {note[i]}")


#imprime mensaje

