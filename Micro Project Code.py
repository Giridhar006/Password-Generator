#Password Generator Project

import random

def low_level_password(nrU_letters,nrL_letters,nr_symbols,nr_numbers,cdw):
    #Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91

    def ask_user():
        # Asks the user whether they like the generated password or not.
        print("To select Yes, please enter 1.")
        print("To select No, please enter 2.")
        ask = input()
        if ask == '1':
            print("Thankyou")
        elif ask == '2':
            low_level_password(nrU_letters,nrL_letters,nr_symbols,nr_numbers,cdw)
        else:
            print("Invalid option")
            ask_user()
            
    global password
    password = ""
    for i in range(0, nrU_letters):
        # ASCII values of capital letters (65 to 90)
        if i not in cdw:
            password += chr(random.randint(65,90))
    for i in range(0, nrL_letters):
        # ASCII values of small letters (97 to 122)
        if i not in cdw:
            password += chr(random.randint(97,122))
    nr_s = nr_symbols
    while nr_s > 0:
        # ASCII values of special characters (33 to 47), (58 to 64), (91 to 96), (123 to 126)
        k = random.randint(33, 126)
        if i not in cdw:
            if not chr(k).isalnum():
                password += chr(k)
                nr_s -= 1
    for i in range(0, nr_numbers):
        # ASCII values of numbers (48 to 57)
        if i not in cdw:
            password += chr(random.randint(48,57))
    print(f"Here is your low level password: {password}")
    print("Do you want to set this as your password?\n")
    ask_user()
    
def high_level_password(nrU_letters,nrL_letters,nr_symbols,nr_numbers,cdw):
    #High Level - Order of characters randomised:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    
    def ask_user():
        # Asks the user whether they like the generated password or not.
        print("To select Yes, please enter 1.")
        print("To select No, please enter 2.")
        ask = input()
        if ask == '1':
            print("Thankyou")
        elif ask == '2':
            high_level_password(nrU_letters,nrL_letters,nr_symbols,nr_numbers,cdw)
        else:
            print("Invalid option")
            ask_user()

    l_U = nrU_letters
    l_L = nrL_letters
    s = nr_symbols
    n = nr_numbers

    t = l_U + l_L + s + n

    global password
    password = ""

    while True:
        a = random.randint(0, 3)
        if l_U != 0 and a == 0:
            # ASCII values of capital letters (65 to 90)
            p = random.randint(65,90)
            if p not in cdw:
                password += chr(p)
                l_U -= 1
            
        elif l_L != 0 and a == 1:
            # ASCII values of small letters (97 to 122)
            p = random.randint(97,122)
            if p not in cdw:
                password += chr(p)
                l_L -= 1
            
        elif s != 0 and a == 2:
            # ASCII values of special characters (33 to 47), (58 to 64), (91 to 96), (123 to 126)
            i = random.randint(33, 126)
            if i not in cdw:
                if not chr(i).isalnum():
                    password += chr(i)
                    s -= 1
            
        elif n != 0 and a == 3:
            # ASCII values of numbers (48 to 57)
            p = random.randint(48,57)
            if p not in cdw:
                password += chr(p)
                n -= 1
            
        if len(password) == t:
            break
    print(f"Here is your high level password: {password}")
    print("Do you want to set this as your password?\n")
    ask_user()

def password_update(website):
    # Updates the existing password
    a = password + "\n"
    filename = website
    with open(filename, "a") as f:
        f.write(a)
        
def view_password():
    # displays the present passwords for a website
    try:
        web = input("Which website do you need your password for?\n")
        website = web.lower()
        website += ".txt"
        with open(website, 'r') as file:
            password = file.readlines()[-1]
            print(password)
    except FileNotFoundError:
        print(f"No password has been generated for {web}. Please generate a new password.\n")
        view_password()
        
def view_password_history():
    # displays all passwords for a website
    try:
        web = input("Which website's password history would you like to see?\n")
        website = web.lower()
        website += ".txt"
        with open(website, 'r') as file:
            passwords = file.readlines()
            for i in passwords:
                print(i)
    except FileNotFoundError:
        print(f"No password has been generated for {web}. Please generate a new password.\n")
        view_password_history()

def U_L():
    while True:
        try:
            nrU_letters = int(input("How many uppercase letters would you like in your password?\n"))
            return nrU_letters
        except:
            print("The option you selected is not valid. Please choose again.\n")
def L_L():
    while True:
        try:
            nrL_letters = int(input("How many lowercase letters would you like in your password?\n"))
            return nrL_letters
        except:
            print("The option you selected is not valid. Please choose again.\n")

def S():
    while True:
        try:
            nr_symbols = int(input(f"How many symbols would you like to include in your password?\n"))
            return nr_symbols
        except:
            print("The option you selected is not valid. Please choose again.\n")

def N():
    while True:
        try:
            nr_numbers = int(input(f"How many numbers would you like to include in your password?\n"))
            return nr_numbers
        except:
            print("The option you selected is not valid. Please choose again.\n")

def C_D_W():
    return list(map(ord,input("Please enter the characters you don't want in your password.\n")))

def check_Key(file_path):
    try:

        # Open the file in read mode
        with open(file_path, 'r') as file:

            # Read the content of the file
            file_content = file.read()

            if not file_content:
                with open(file_path, 'w') as new_file:
                    
                    content = input("Please set a password for the password generator.\n")
                    new_file.write(content)
                    print("Great! Your password has been set.")
                    return 1
            else:

                # Prompt the user for input
                user_input = input("Please enter the password for the password generator.\n")

                # Compare user input with file content
                if user_input == file_content:
                    print("Great! The password has been entered correctly.")
                    return 1
                else:
                    print("I apologize for the inconvenience. Please try entering the password again.")
                    check_Key(file_path)
                    return 1   
    except FileNotFoundError:

        # Create a new file
        with open(file_path, 'w') as new_file:
            content = input("Please set a password for the password generator.\n")
            new_file.write(content)
            print("Great! Your password has been set.")
            return 1


def update_Key(file_path):

    # Prompt the user for new content
    new_content = input("To change the password for the password generator, please enter the new desired password.\n")

    # Open the file in write mode and overwrite the content
    with open(file_path, 'w') as file:
        file.write(new_content)

    print("Excellent! The password for the password generator has been successfully updated.")
    print("Thankyou")

def option():
    if k == 1:
        print()
        print("To generate a low-level password, please enter 1.")
        print("To generate a high-level password, please enter 2.")
        print("To view your passwords, please enter 3.")
        print("To view the password history for a particular website, please enter 4.")
        print("To update the password for the password generator, please enter the number 5.")
        print()

        opt = input()

        if opt == '1':
            web = input("Which website would you like to generate a password for?\n")
            website = web.lower()
            website += ".txt"
            nrU_letters = U_L()
            nrL_letters = L_L()
            nr_symbols = S()
            nr_numbers = N()
            cdw = C_D_W()
            low_level_password(nrU_letters,nrL_letters,nr_symbols,nr_numbers,cdw)
            password_update(website)

        elif opt == '2':
    
            web = input("Which website would you like to generate a password for?\n")
            website = web.lower()
            website += ".txt"
            nrU_letters = U_L()
            nrL_letters = L_L()
            nr_symbols = S()
            nr_numbers = N()
            cdw = C_D_W()     
            high_level_password(nrU_letters,nrL_letters,nr_symbols,nr_numbers,cdw)
            password_update(website)

        elif opt == '3':
            view_password()
            
        elif opt == '4':
            view_password_history()
            
        elif opt == '5':
            update_Key(file_path)

        else:
            print("The option you selected is not valid. Please choose again.\n")
            option()

print("Welcome to the Password Generator!\n")

file_path = 'key.txt'
k = check_Key(file_path)
option()