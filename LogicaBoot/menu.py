RUTA1 = 'G:\My Drive\Projectos de Software\PROYECTOS\Curso_Python\PC_WINDOWS\LogicaBoot\AltaUser.txt'
RUTA2 = 'G:\My Drive\Projectos de Software\PROYECTOS\Curso_Python\PC_WINDOWS\LogicaBoot\AltaPass.txt'
userFile = open(RUTA1,"w+") # Leer + Escribir
print(userFile.readable())
passwordFile = open(RUTA2,"w+") # Leer + Escribir)
print(passwordFile.readable())


def run():
    pass

Menu = '''
Bien venido al menu de ...

OPC 1.- Alta de Usuario
OPC 2.- Inicio de Sesion
OPC 3.- Salir del modulo

Elige la Opcion de Incio: '''

opcion = int(input(Menu))

if opcion == 1:
    newUser = input('Dame tu nobre de usuario: ')
    newpass = input('Escribe la contraseña: ')
    validaPass = input('Confirma la contraseña: ')
    if newpass == validaPass:
        print('Se ha creado la Cuenta: ' + newUser +' con Exito')
        userFile.write(newUser)
        passwordFile.write(newpass)
    else:
        print('Vuelve a intentar el alta de usuario: ')

elif opcion == 2:
    logUsuario = input('ingresa cuenta de Usuario: ')
    logpass = input('Ingresa la Contraseña: ')
    print(passwordFile.readline() + userFile.readline())

    if logpass == passwordFile and logUsuario == userFile:
        print('Acceso concedido: ')
    else:
        print('Acceso Denegado: ')
elif opcion == 3:
    print('Gracias por visitarnos: ')
else:
    print('Solo son 3 Opciones:')


if __name__ =='__main__':
    run()
