# Fuente:Ejercicio del Libro Automate the Boring Stuff with Python
# @Al Sweigart
# @darkgosh 
# Practica de Loops
# (p. 109)
# Date 20240709

'''
Descripcion delejercicio......
'''
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
