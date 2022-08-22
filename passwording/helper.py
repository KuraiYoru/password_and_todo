import random

def password(length, uppercase=False, special=False, numbers=False):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if uppercase:
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if special:
        characters.extend(list('!@#$%^&*()'))
    if numbers:
        characters.extend(list('0123456789'))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return thepassword