# Sweigart, Al. Automate the Boring Stuff with Python . No Starch Press. Edición de Kindle. 
# @darkgosh
# Date: 10/04/2023
# (p. 50)



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