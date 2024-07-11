"""
Curso Basico de Python
Clase No.29 Uso de tuplas
@Platzi
@Darkgosh
V1.0
Date: 21/03/2023
"""

#Las TUPLAS son solo lectura y hacer una DECLARACION. No se pueden crear, ni actualizaar, ni borrar.

def run():
    numeros = [1, 2 ,3, 4, 5]
    print(numeros)
    numeros.append('Hola')
    print(numeros)
    numeros.pop(5)
    print(numeros)
    numeros2 = [6,7,8,9,10]
    listaFinal = numeros + numeros2
    print(listaFinal)
    numeros = [1, 2 ,3, 4, 5] * 5
    print(numeros)
    print('            ')
    mi_tupla = (1,2,3,4,5)
    print(mi_tupla)
    for numero in mi_tupla:
        print(numero)

if __name__ =='__main__':
    run()


numbers = (1,2,3,5) #declaracion
strings = ('nico','zule','santi')
print(numbers)
print('0 =>',numbers[0])
print('- 1', numbers[-1])
print(type(numbers))
      
print(strings)
print(type(strings))

#LISTAS SON CRUD=(crear,read,update, delete)


#Convertir una TUPLA a una LISTA
my_list = list(strings)
print(my_list)
print(type(my_list))

my_list[1] = 'juli'
print(my_list)

#Convertir una LISTA a una TUPLA
my_tuple = tuple(my_list)
print(my_tuple)




  

