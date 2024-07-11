# @darkgosh Ejercicio proporcionados por https://aprendeconalf.es/
# Practica de Estructuras de control
# Date 20240704

'''
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta 
le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además 
de la mozzarella y el tomate que están en todas la pizzas. 
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
'''
#solicita datos

pizza = int(input("Hola Bienvenido a La Pizzeria Bella Napoli \n Para pizzas Vegetariasnas teclea '1' \n para Pizzas No Vegetarianas Teclea '2': " ))
vegana = ["Pimiento", "tofu"]
no_vegana = ["Peperoni","Jamón","Salmón"]
#Estructura de control
if pizza == 1:
    print(f"Escogiste opcion {pizza} Pizza Vegetariana")
    ingredientes_adicional = int(input("tienes derecho a un ingrediente adicional: \n Para Pimiento teclea '1' \n Para Tofu, teclea '2': " ))
    if ingredientes_adicional == 1:
            print(f"Tu Pizza Vegetariana, con {vegana[0]}, estara lista en 20 min")
    elif ingredientes_adicional == 2:
         print(f"Tu Pizza Vegetariana, con {vegana[1]}, estara lista en 20 min")

elif pizza == 2:
    print(f"Escogiste opcion {pizza} Pizza No Vegetariana")    
    ingredientes_adicional = int(input("tienes derecho a un ingrediente adicional: \n Para Peperoni teclea '1' \n Para Jamon, teclea '2'\n Para Salmon Teclea '3': " ))
    if ingredientes_adicional == 1:
            print(f"Tu Pizza No Vegetariana, con {no_vegana[0]}, estara lista en 20 min")
    elif ingredientes_adicional == 2:
         print(f"Tu Pizza No Vegetariana, con {no_vegana[1]}, estara lista en 20 min")
    elif ingredientes_adicional == 3:
         print(f"Tu Pizza No Vegetariana, con {no_vegana[2]}, estara lista en 20 min")     
else:
     print("Opcion No valida, Vuele a intentarlo")
#imprime mensaje

