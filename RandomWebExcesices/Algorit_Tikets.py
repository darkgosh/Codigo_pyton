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
# avi_max = 20
# bus_max = 40
avi_max = 20
bus_max = 40
def datos_ticket(libres, max):

    libres = max -libres
    ciudad_origen = input("Dame la direccion de origen: ") 
    ciudad_destino = input("Dame el destinoÑ ") 
    fecha = input("Dame la Fecha: ") 
    hora = input("Dame la hora: ") 
    return(ciudad_destino,ciudad_origen,fecha,hora, libres)
    
    
while avi_max > 0 or bus_max > 0:
    print("Bienvenido al Marketplace del Viajes Ren ")
    opcion = int(input('Escribe 1 para compra de Boletos de Avion y 2 para la compra de boletos de Autobus : '))
    if opcion == 1:
        print('Elegiste opcion 1 Ticket de Avion ')
        print("Seleccionaste transporte por Avion: ")
        lugar= int(input("¿Cuantos lugares necesitas?: "))
        #avi_max = avi_max - lugar
        ticket = datos_ticket(lugar, avi_max)
        avi_max =int(ticket[4])
        print(ticket)

    elif opcion == 2:
        print('Elegiste opcion 2 Ticket de Autobus')
        print("Seleccionaste transporte por Autobus: ")
        lugar= int(input("¿Cuantos lugares necesitas?: "))
        ticket = datos_ticket(lugar, bus_max)
        bus_max =int(ticket[4])
        print(ticket)
    else:
        print('escribe la opcion correcta')




