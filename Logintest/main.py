
import os

data=''
loginQuestion=''
hasAccount = False

#LOGIN
def loginFunction(username, password):
    username = input('\nLOGIN\nenter your username: ')
    password = input('enter your password: ')
    with open('Data.txt', 'r') as file:
        users = file.readlines()
        for user in users:
            stored_user, stored_pass = user.strip().split('|')
            if username == stored_user and password == stored_pass:
                print('login successful!')
                return
    loginQuestion=input('INVALID USERNAME OR PASSWORD\ntry again (y) or register (n) - ')
    if loginQuestion == 'y':
        loginFunction(username, password)
    elif loginQuestion == 'n':
        registerFunction(username, password)
    else:
        print('INVALID INPUT, RETURNING TO LOGIN')
        loginFunction(username, password)


#REGISTER
def registerFunction(username, password):
    while True:
        username=input(f'\nREGISTRATION\nenter a Username: ')
        if os.path.exists('Data.txt'):
            with open('Data.txt', 'a+') as data:
               data.seek(0)
               if any(username in line for line in data):
                   print("username already registered, try another!")
                   loginQuestion=''
                   registerFunction(username, password)
               else:
                   password=input(f'\nPASSWORD\nenter a Password: ')
                   data.write(f'{username}|{password}\n')
                   data.flush()
                   print('REGISTRATION SUCCESFULL!')
                   loginQuestion=input('would you like to login? y/n ')
            if loginQuestion=='y':
                loginFunction(username, password)
                break
            elif loginQuestion=='n':
                print('exiting')
                break
            else:
                break
        else:
            with open('Data.txt', "w+") as data:
                password = input(f'\nPASSWORD\nenter a Password: ')
                data.write(f'{username}|{password}\n')
                data.flush()
                print('REGISTRATION SUCCESFULL!')
                loginQuestion=input('would you like to login? y/n ')
                if loginQuestion=='y':
                    loginFunction(username, password)
                else:
                    print('exiting')
                    break


#ACCOUNT CHECK
while True:
    accountCheck=str(input("do you have an account? - y/n ")).lower()
    if accountCheck=="y":
        loginFunction(data, data)
        break
    elif accountCheck=="n":
        loginQuestion=input("would you like to register one? - y/n ")
        if loginQuestion=="y":
            registerFunction(data, data)
        else:
            print('exiting')
        break
    else:
        print("enter y/n")




