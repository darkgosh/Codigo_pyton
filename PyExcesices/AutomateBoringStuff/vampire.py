# Sweigart, Al. Automate the Boring Stuff with Python . No Starch Press. Edición de Kindle. 
# @darkgosh
# Date: 10/04/2023
# (p. 50)
#ELIF statements
name = input("Cual es tu nombre: ")
age = int(input("cual es tu edad: "))

if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
