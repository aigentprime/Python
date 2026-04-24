"""
🧠 Challenge: Build a User Password Manager
🎯 Goal

Create a Python program that lets the user:

Add a new user + password
View all saved users
Search for a user
Exit the program

And most importantly:

👉 Data must stay saved even after closing the program

That means you must use JSON + files correctly.

import os
import json
FILE = "Practice\\Day_5\\file.json"
def load_data():
    if os.path.exists(FILE):
        with open(FILE,"r") as f:
            dct = json.load(f)
        return dct
    else:
        with open(FILE,"w") as f:
            json.dump({},f,indent=4)
            return {}
def add_account():
    account = input("Enter name of account E.g. gmail: ")
    password = input("Enter password: ")
    data = load_data()
    if account in data:
        user_choice_2 = input(f"{account} account exists overwrite? (y/n)?").lower()
        if user_choice_2 == "y":
            data[account] = password
            with open(FILE,"w") as f:
                json.dump(data,f,indent=4)
            print(f"{account} with {password} added succesfully")
        elif user_choice_2 == "n":
            print("Account not added")
        else:
            print("Please enter valid input(y/n)")
    else:
        data[account] = password
        with open(FILE,"w") as f:
            json.dump(data,f,indent=4)
        print(f"{account} with {password} added succesfully")

def view_accounts():
    data = load_data()
    if not data:
        print("No accounts found")
    else:
        for k,v in data.items():
            print(k,v)
        return data    

def search_account():
    data = load_data()
    account = input("Enter name of account E.g. gmail: ")
    if account in data:
        print(f"Found: {account} password: {data[account]}")
    else:
        print(f"Account does not exists")
while True:
    user_choice = input(
        "Enter operation:(1-2-3-4)\n"
        "1. Add account\n"
        "2. View accounts\n"
        "3. Search account\n"
        "4. Exit\n"
    )

    if user_choice.isdigit():
        if user_choice == "1":
            add_account()
        elif user_choice == "2":
            view_accounts()
        elif user_choice == "3":
            search_account()
        elif user_choice == "4":
            break
        else:
            print("Please enter valid input (1-2-3-4)")
    else:
        print("Please enter numbers only")
        
"""

