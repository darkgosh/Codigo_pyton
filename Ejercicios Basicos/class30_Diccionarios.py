"""
Curso Basico de Python
Clase No.30 Diccionarios
@Platzi
@Darkgosh
V1.0
Date: 21/03/2023
"""
#un diccionarios es una estructura de datos de llaves y valores, se acceder atraves de sus llaves.
 
def run():
    mi_diccionario = {
        'llave1' : 1,
        'llave2' : 2,
        'llave3' : 3,
    }
    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])
    poblacion_paises = {
        'Argentina' : 44938712,
        'Brasil'    : 210147125,
        'Colombia'  : 50372424,
    }
    # print(poblacion_paises['Argentina'])
    # for pais in poblacion_paises.keys():
    #     print(pais)
    # for pais in poblacion_paises.values():
    #     print(pais)
    for pais, poblacion  in poblacion_paises.items():
        print(pais + ' Tiene ' + str(poblacion) + ' habitantes. ')

if __name__ =='__main__':
    run()
