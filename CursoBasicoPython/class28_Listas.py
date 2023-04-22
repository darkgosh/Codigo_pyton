"""
Curso Basico de Python
Clase No.28 Uso de listas
@Platzi
@Darkgosh
V1.0
Date: 21/03/2023
"""

def run():
    objetos = ['Hola', 3, 4.5, True, 1]
    for elementos in objetos:
        print(elementos)
    print(objetos[::-1])
    print(objetos[1:3])

    # newElemento = input('Escribre un nuevo elemento: ')
    # newElemento = objetos.append(newElemento)

    '''
    append(): Añade un ítem al final de la lista.
    clear(): Vacía todos los ítems de una lista.
    extend(): Une una lista a otra.
    count(): Cuenta el número de veces que aparece un ítem.
    index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
    insert(): Agrega un ítem a la lista en un índice específico.
    pop(): Extrae un ítem de la lista y lo borra.
    remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
    reverse(): Le da la vuelta a la lista actual.
    sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.
    '''


    numbers  = [1,2,3,4,5]
    print(numbers)

    numbers[-1] = 10
    print(numbers)

    numbers.append(700) #agregar .append
    print(numbers)

    numbers.insert(0,"Hola")
    print(numbers)
    
    numbers.insert(3,"CHANGE")
    print(numbers)
    
    tasks = ["todo 1","todo 2","todo 3"]
    new_list = numbers + tasks
    print(new_list)

    index = new_list.index("todo 2")
    new_list[index] = "cambio"
    print(new_list)
    
    new_list.remove("todo 1")
    print(new_list)
    
    new_list.pop()
    print(new_list)

    new_list.pop(0)
    print(new_list)

    new_list.reverse()
    print(new_list)

    numbers_a = [1,4,6,3]
    numbers_a.sort()#ordena
    print(numbers_a)

    numbers_a = ['re','ab','ed']
    numbers_a.sort()#ordena
    print(numbers_a)


'''
En este desafío, se te proporcionará una lista de letras llamada letters. Tu reto es realizar las siguientes operaciones en orden:

Agregar la letra G al final de la lista.
Reemplazar la letra en la posición 0 con la letra Z.
Eliminar la letra C de la lista.
Imprimir la lista resultante al revés.
Ejemplo:

Input: ["A", "B", "C", "D", "E", "F"]
Output: ["G", "F", "E", "D", "B", "Z"]

Recuerda que debes realizar las operaciones en el orden indicado y utilizar las funciones y métodos de las listas de Python apropiados para cada tarea.

'''
letters = ['A', 'B', 'C', 'D', 'E', 'F']
# Escribe tu solución 👇
letters.append('G')
index = letters.index('A')
letters[index] = 'Z'
letters.remove('C')
letters.reverse()
print(letters)




if __name__ =='__main__':
    run()
