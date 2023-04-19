"""
Curso de Algoritmos y pensamiento Logico
Clase No.18 Metodos con Cadenas de Caracteres.
@Platzi
@Darkgosh
V1.0
Date: 19/04/2023
"""
"""
VENTA DE TICKETS
En una empresa de viajes se requiere realizar la venta de tickets teniendo en cuenta las siguientes consideraciones:
 * Cada tickets incluye 
    ciudad de origen, 
    ciudad de destino, 
    fecha, 
    hora, 
    cantidad de puestos y 
        Datos del pasajero:
            Nombre,
            Apellidos,
            Edad,
            Sexo
 * Cada autobús o avión tiene una capacidad máxima de pasajeros, debo avisar cuando se hayan llenado los cupos.
 * Debes asignar los puestos de cada medio de transporte conforme al orden de compra.
"""
lugar = 0
avi_max = 20
bus_max = 40

    

while avi_max and bus_max >= 0:
    print("Bienvenido al Marketplace del Viajes Ren ")
    opcion = int(input('Escribe 1 para compra de Boletos de Avion y 2 para la compra de boletos de Autobus : '))
    if opcion == 1:
        print('Elegiste opcion 1 Ticket de Avion ')
        print("Seleccionaste transporte por Avion: ")
        lugar= int(input("¿Cuantos lugares necesitas?: "))
        avi_max = avi_max - lugar
        datos_ticket()
    elif opcion == 2:
        print('Elegiste opcion 2 Ticket de Autobus')
        print("Seleccionaste transporte por Autobus: ")
        lugar= int(input("¿Cuantos lugares necesitas?: "))
        bus_max = bus_max - lugar
        datos_ticket()
    else:
        print('escribe la opcion correcta')

def datos_ticket():
    ciudad_origen = input("") 
    ciudad_destino = input("") 
    fecha = input("") 
    hora = input("") 
    return datos_ticket



