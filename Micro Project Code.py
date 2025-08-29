#Password Generator Project

import random
import pickle

filename = "passwords.pkl"

def ask_user(opt, nrU_letters, nrL_letters, nr_symbols, nr_numbers, cdw):
    # Asks the user whether they like the generated password or not.
    print("To select Yes, please enter 1.")
    print("To select No, please enter 2.")
    ask = input()
    if ask == '1':
        print("Thankyou")
    elif ask == '2':
        if opt == "low":
            low_level_password(nrU_letters, nrL_letters, nr_symbols, nr_numbers, cdw)
        elif opt == "high":
            high_level_password(nrU_letters,nrL_letters,nr_symbols,nr_numbers,cdw)
    else:
        print("Invalid option")
        ask_user()

def low_level_password(nrU_letters, nrL_letters, nr_symbols, nr_numbers, cdw):
    #Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91

    global password
    password = ""

    nrU_l = nrU_letters
    while nrU_l > 0:
        # ASCII values of capital letters (65 to 90)
        i = chr(random.randint(65,90))
        if i not in cdw:
            password += i
        nrU_l -= 1

    nrL_l = nrL_letters
    while nrL_l > 0:
        # ASCII values of small letters (97 to 122)
        i = chr(random.randint(97,122))
        if i not in cdw:
            password += i
        nrL_l -= 1

    nr_s = nr_symbols
    while nr_s > 0:
        # ASCII values of special characters (33 to 47), (58 to 64), (91 to 96), (123 to 126)
        i = chr(random.randint(33, 126))
        if i not in cdw and not i.isalnum():
            password += i
            nr_s -= 1

    nr_n = nr_numbers
    while nr_n > 0:
        # ASCII values of numbers (48 to 57)
        i = chr(random.randint(48,57))
        if i not in cdw:
            password += i
        nr_n -= 1

    print(f"Here is your low level password: {password}")
    print("Do you want to set this as your password?\n")
    ask_user("low", nrU_letters, nrL_letters, nr_symbols, nr_numbers, cdw)

def high_level_password(nrU_letters,nrL_letters,nr_symbols,nr_numbers,cdw):
    #High Level - Order of characters randomised:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

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
            if i not in cdw and not chr(i).isalnum():
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
    ask_user("high", nrU_letters, nrL_letters, nr_symbols, nr_numbers, cdw)

def password_update(username, website):

    try:
        # Updates the existing password
        with open(filename, "rb") as file:
            data = pickle.load(file)

        if website in data:
            if username in data[website]:
                data[website][username].append(password)          # add password at the end
            else:
                data[website][username] = [password]
        else:
            data[website] = {}
            data[website][username] = [password]

        with open(filename, "wb") as file:
            pickle.dump(data, file)

    except:
        # Creates new file and adds new password
        data = {}
        with open(filename, "wb") as file:
            data[website] = {}
            data[website][username] = [password]
            pickle.dump(data, file)

def view_password():
    # displays the present passwords for a website

    website = input("Which website do you need your password for?\n")
    website = website.lower()

    with open(filename, 'rb') as file:
        data = pickle.load(file)
    if website in data:
        username = input("For which username do you need your password for?\n")
        if username in data[website]:
            password = data[website][username][-1]
            print(password)
            file.close()
        else:
            print(f"No password has been generated for the website \"{website}\" with the username \"{username}\". Please generate a new password.\n")
    else:
        print(f"No password has been generated for the website \"{website}\". Please generate a new password.\n")

def view_password_history():
    # displays all passwords for a website
    website = input("Which website's password history would you like to see?\n")
    website = website.lower()

    with open(filename, 'rb') as file:
        data = pickle.load(file)
    if website in data:
        username = input("For which username do you need your password for?\n")
        if username in data[website]:
            passwords = data[website][username]
            for i in passwords:
                print(i)
            file.close()
        else:
            print(f"No password has been generated for the website \"{website}\" with the username \"{username}\". Please generate a new password.\n")
    else:
        print(f"No password has been generated for the website \"{website}\". Please generate a new password.\n")

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

def check_Key():
    try:
        # Open the file in read mode
        with open(filename, 'rb') as file:
            # Read the content of the file
            data = pickle.load(file)

        if "default" not in data:
            file.close()

            p_1 = input("Please set a password for the password generator.\n")
            p_2 = input("Confirm password.\n")
            if p_1 == p_2:
                data = {}
                data["default"] = p_1
                with open(filename, 'wb') as file:
                    pickle.dump(data, file)
                file.close()
                print("Great! Your password has been set.")
                check_Key()
            else:
                print("passwords do not match, please try again.")
                check_Key()
        else:
            # Prompt the user for input
            p = input("Please enter the password for the password generator.\n")

            # Compare user input with file content
            if p == data["default"]:
                print("Great! The password has been entered correctly.")
                file.close()
            else:
                print("I apologize for the inconvenience. Please try entering the password again.")
                file.close()
                check_Key()

    except FileNotFoundError:
        # Create a new file
        data = {}
        with open(filename, "wb") as file:
            pickle.dump(data, file)
        check_Key()

def update_Key():
    # Prompt the user for new content
    p_1 = input("To change the password for the password generator, please enter the new desired password.\n")
    p_2 = input("Confirm password.\n")

    if p_1 == p_2:
        # Open the file in write mode and overwrite the content
        with open(filename, "rb") as file:
            data = pickle.load(file)
        file.close()

        data["default"] = p_1
        with open(filename, "wb") as file:
            pickle.dump(data, file)
        file.close()
    else:
        print("Passwords do ont match, please try again.")
        update_Key()

    print("Excellent! The password for the password generator has been successfully updated.")
    print("Thankyou")

def option():
    print()
    print("To generate a low-level password, please enter 1.")
    print("To generate a high-level password, please enter 2.")
    print("To view your passwords, please enter 3.")
    print("To view the password history for a particular website, please enter 4.")
    print("To update the password for the password generator, please enter the number 5.")
    print()

    opt = input()

    if opt == '1':
        website = input("Which website would you like to generate a password for?\n")
        website = website.lower()
        username = input("For which username would you like to generate a password for?\n")
        nrU_letters = U_L()
        nrL_letters = L_L()
        nr_symbols = S()
        nr_numbers = N()
        cdw = C_D_W()
        low_level_password(nrU_letters, nrL_letters, nr_symbols, nr_numbers, cdw)
        password_update(username, website)

    elif opt == '2':

        website = input("Which website would you like to generate a password for?\n")
        website = website.lower()
        username = input("For which username would you like to generate a password for?\n")
        nrU_letters = U_L()
        nrL_letters = L_L()
        nr_symbols = S()
        nr_numbers = N()
        cdw = C_D_W()     
        high_level_password(nrU_letters, nrL_letters, nr_symbols, nr_numbers, cdw)
        password_update(username, website)

    elif opt == '3':
        view_password()

    elif opt == '4':
        view_password_history()

    elif opt == '5':
        update_Key()

    else:
        print("The option you selected is not valid. Please choose again.\n")
        option()

print("Welcome to the Password Generator!\n")

check_Key()
option()