import json
import time as t


def users():
    with open('user_details/user_details.json', 'r') as f:
        data = json.load(f)
    return data
    
def instruction():
    print('To Continue, Please choose from any of the options below\n')
    print('1. START QUIZ')
    print('2. ABOUT')
    print('3. EXIT')
    

def home_page(username, user, password):
    if username in user.keys() and password == user[username]:
        if username == 'Admin':
            print(f'\nWELCOME TO TESTING CENTRE BOLUWATIFE')
            print('---------------------------------------')
            t.sleep(2)
            instruction()
        else:
            print(f'\nWELCOME TO TESTING CENTRE {username.upper()}')
            print('-----------------------------------------------')
            t.sleep(2)
            instruction()
            

def login():
    '''This code loads the user details file, and confims if the
    entered details correlate with any of the data, sign up the user
    if his/her name is not present.'''
    
    with open('user_details/user_details.json', 'r+') as user_details:
        user = json.load(user_details)
        username = input('Username: ')
        password = input('Password: ')
        if username in user.keys():
            while password != user[username]:
                print('Incorrect password!Please, Try Again\n')
                username = input('Username: ')
                password = input('Password: ')
            else:
                t.sleep(1.5)
                print('Login successful!')
                t.sleep(1.5)
        else:
            print('\nYour account is not in the database')
            t.sleep(2)
            print('Wait while we create an account for you')
            t.sleep(1)
            user.update({username:password})
            
            user_details.seek(0)
            json.dump(user, user_details)
            user_details.truncate()
            print('\nAccount successfully created!')
            t.sleep(1)
    home_page(username, user, password) 

def about():
    print('''
This is a multi choice question mini project done by DURODOLA BOLUWATIFE,
a student of  DSC (Developer Student Clubs) FUTA Novice Class.
* This program is  not perfect yet, but will be improved subsequently.
e-mail: punctuallee@gmail.com''')

    

        
    
    

    