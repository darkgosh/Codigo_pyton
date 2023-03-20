RUTA = 'G:\My Drive\Projectos de Software\PROYECTOS\Curso_Python\PC_WINDOWS\LogicaBoot\passFile.txt'
passwordFile = open(RUTA)
secretPassword = passwordFile.read()
print(secretPassword)
name = input('Cual es tu nombre? ')
edad = int(input('Cual es tu edad: '))


def run():
    if name == "Ren":
      print('Hi Ren')
    elif edad < 12:
      print('You are not Ren, Kiddo.')
    else:
      print('Hello Stranger')
      




    print('Enter your PassWord')
    typePassword = input()
    if typePassword == secretPassword:
     print('Acces Granted')
    elif typePassword == "12345":
     print ('That password is one that an idiot puts on their luggage. ')
    else:
     print('Acces denied !! ')

passwordFile.close()
if __name__ == '__main__':
    run()
