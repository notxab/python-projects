import string
import random

# generates password
def passwordGenerator(size=15, chars=string.ascii_uppercase + string.ascii_lowercase + string.ascii_letters + string.digits):

    password = ''.join(random.choice(chars) for _ in range(size))

    with open('passwords.txt', 'a') as file:
        file.write(f"{password}\n")
        file.close()
    return password

def initialize():
    while True:
        init = input('would you like to generate one or multiple passwords?\n(y/n)\n')
        if init == 'y':
            print('password generated!\n---------------')
            print(f"{passwordGenerator()}")
            break
        else:
            passwordAmount = int(input('how many passwords would you like to generate?\n'))
            for i in range(passwordAmount):
                password = passwordGenerator()
                print(password)
            print(f'\nDone generating {passwordAmount} passwords!\n')
            break


initialize()


