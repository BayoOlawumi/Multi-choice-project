#! python3
import time as t
from codes import homepage,selection


print("""
BEFORE YOU PROCEED, READ THE INSTRUCTIONS BELOW:
1. You can't access the content of this program until you login
2. If you are a new user, Continue....
3. Note that all entries are case sensitive
""")
t.sleep(7)
print("LOGIN/SIGNUP PAGE")
print("*****************")
homepage.login()
users = homepage.users()


if __name__ == "__main__":
    option = 0
    while option != '3' or 'EXIT':
        option = input('\nEnter an option to proceed: ').upper()
        if option == '1' or option == 'START QUIZ':
            selection.choose_category()
        elif option == '2' or option == 'ABOUT':
            homepage.about()
        elif option == '3' or option == 'EXIT':
            print("Thanks!, we'll love to see you around some other time")
            break
        else:
            print("Invalid input, please check and try again")
        
    
