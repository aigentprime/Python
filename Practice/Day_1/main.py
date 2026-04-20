"""
🧠 Python Practice Questions (Beginner Level)
1.Print Basics
Write a program that prints:
Hello, Python!
2.Variables
Create a variable called name and assign your name to it. Then print:
My name is ___
3.User Input
Ask the user for their age and print:
You are ___ years old.
4.Simple Math
Take two numbers from the user and print their sum.
5.Even or Odd
Ask the user for a number and print whether it is even or odd.
6.If-Else Practice
Ask the user for a number.
If it's greater than 10, print "Big number!"
Otherwise, print "Small number!"
7.For Loop
Print numbers from 1 to 10 using a loop.
8.List Basics
Create a list of 5 fruits and print each fruit using a loop.
9.String Manipulation
Ask the user for a word and print it reversed.
10.Mini Challenge
Create a simple calculator:
Ask for two numbers
Ask for an operation (+, -, *, /)
Print the result
"""

"""print("Hello, Python!") #print() is a built-in function prints passed argument to the screen

name = "Tunç"
print("My name is",name)

age = input("Enter your age: ")
print("You are "+age+" years old")

input_1 = int(input("Enter number 1: "))
input_2 = int(input("Enter number 2: "))
print("Sum of numbers are:",input_1+input_2)

number = int(input("Enter number: "))
print("Even" if number%2 == 0 else "Odd")

number = int(input("Enter number: "))
print("Big number!" if number > 10 else "Small number!")

for i in range(1,11):
    print(i)

fruits = ["apple","orange","banana","cherry","watermelon"]
for i in fruits:
    print(i)

word = input("Enter a word: ")
print(word[::-1])

number_1 = int(input("Enter a number"))
number_2 = int(input("Enter a number"))
op = input("Enter operation (+, -, *, /)")
if op == "+":
    print(number_1 + number_2)
elif op == "-":
    print(number_1 - number_2)
elif op == "*":
    print(number_1 * number_2)
elif op == "/":
    if number_2 != 0:
        print(number_1 / number_2)
    else:
        print("Cannot divide by 0!")
else:
    print("Invalid operation")
    """
"""
🧠 Intermediate Beginner Exercises (Loops + Logic)
1. Count Even Numbers

Ask the user for a number n.
Print how many even numbers exist between 1 and n.

👉 Example:
Input: 10 → Output: 5 (2,4,6,8,10)

2. Sum of Digits

Ask the user for a number (e.g., 1234).
Calculate and print the sum of its digits.

👉 Output: 1 + 2 + 3 + 4 = 10

3. Multiplication Table

Ask the user for a number and print its multiplication table up to 10.

👉 Example for 3:

3 x 1 = 3
3 x 2 = 6
...
4. Reverse a Number (No slicing)

Ask the user for a number and reverse it using a loop.

👉 Input: 1234 → Output: 4321
🚫 Don’t use [::-1]

5. Number Guessing Game
Generate a secret number (1–10)
Keep asking the user to guess
Tell them “Too high” / “Too low”
Stop when correct

💡 Hint: use while loop

6. Prime Number Check

Ask the user for a number and check if it’s prime.

👉 Example:

7 → Prime
8 → Not prime

💡 This is a classic logic challenge—take your time.

7. Fibonacci Sequence

Ask for n and print first n Fibonacci numbers.

👉 Example (n=5):

0 1 1 2 3
8. Find the Largest Number

Ask the user to enter 5 numbers (one by one).
Print the largest number.

🚫 Don’t use max()

9. Pattern Printing

Print this pattern:

*
**
***
****
*****

💡 Nested loops time.

10. Password Attempts
Set a correct password (e.g., "python123")
Let the user try 3 times
If correct → “Access granted”
If not → “Access denied”

number = int(input("Enter a number"))
counter = 0
lst = []
for i in range(2,number+1):
    if i % 2 == 0:
        lst.append(i)
        counter += 1
print(f"Output: {counter}", tuple(lst))

number = input("Enter a number: ")
suma = 0
for i in number:
    suma += int(i)
print(suma)

number = int(input("Enter a number"))
for i in range(1,11):
    print(f"{number} * {i} = ",number * i )

number = input("Enter a number")
reverse = ""
length = len(number) -1
while length >= 0:
    reverse += number[length]
    length -= 1
print(reverse)

import random
number = random.randint(1,10)
is_correct = True
while is_correct:
    user_guess = int(input("Enter a number between 1-10 inclusive: "))
    if user_guess > number:
        print("Too High!")
    elif user_guess < number:
        print("Too Low!")
    else:
        print("Correct")
        is_correct = False

def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
print(isPrime(19))

number = int(input("Enter a number"))
number_1 = 0
number_2 = 1
for i in range(number):
    print(number_1)
    number_1,number_2 = number_2,number_1+number_2 

lst = []
for i in range(5):
    number = int(input("Enter a number: "))
    lst.append(number)
largest = lst[0]
for i in lst:
    if i >= largest:
        largest = i
print(largest) 

for i in range(1,6):
    print(i*"*") 

password = "python123"
chances = 3
while chances > 0:
    user_guess = input("Enter password: ")
    if user_guess == password:
        print("Access granted")
        break
    else:
        chances -=1 
        if chances == 0:
           print("Access denied permanently")
           break
        print("Access denied!")  """
        
"""
🚀 Mini Project 1: Number Guessing Game (Improved)

You already did a basic version—now upgrade it.

✅ Requirements:
Random number between 1–100
Count how many attempts the user takes
Give hints:
“Very close” (difference ≤ 3)
“Too high” / “Too low”
After correct guess:
Print attempts
Ask: “Play again? (y/n)”
💡 Goal:

Learn:

loops inside loops
better game flow
user experience        



import random
number = random.randint(1,100)
play_again = True
attempt = 0
while play_again:
    user_guess = int(input("Enter a number"))
    attempt += 1
    print(f"Attempt :{attempt}")
    if user_guess == number:
        print("Correct")
        play_again = input("Play again? (y/n): ").lower()
        number = random.randint(1,100)
        attempt = 0
        if play_again == "y":
            play_again = True
        else:
            play_again = False
    elif abs(user_guess - number) <= 3:
        print("Very close")
    elif user_guess > number :
        print("Too high")
    elif user_guess < number:
        print("Too low")"""

"""
🧮 Mini Project 2: Simple Banking System
✅ Features:
Start with balance = 1000
Show menu:
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Rules:
Deposit → add money
Withdraw → subtract money
❗ Don’t allow negative balance
Loop until user exits
💡 Goal:

Learn:

while loops with menus
state management (balance changes over time)
input validation

    
def bank():
    balance = 1000
    while True:
        print("1. Check Balance")    
        print("2. Deposit")   
        print("3. Withdraw")   
        print("4. Exit")
        try:
            user_input = int(input("Enter 1-4: "))
        except ValueError:
            print("Invalid input. Enter a number.")
            continue
        if user_input == 1:
            print(f"Balance :${balance}")
        elif user_input == 2:
            depo = float(input("Enter deposit amount")) 
            if depo <= 0:
                print("Invalid deposit amount")
            else:
                balance += depo
                print(f"Added {depo} amount.")
        elif user_input == 3:
            withdraw = float(input("Enter withdraw amount"))
            if withdraw <= 0:
                print("Invalid amount")
            elif withdraw > balance:
                print("Insufficient funds")
            else:
                balance -= withdraw
                print(f"Withdrawn {withdraw} amount")
        elif user_input == 4:
            print("Goodbye!")
            break
bank()        
"""

"""
🔐 Mini Project 3: Login System with Lockout
✅ Requirements:
Predefined username & password
User must enter both correctly
Max 3 attempts
Advanced Features:
After 3 failed attempts → lock system
Show how many attempts left each time
If login successful → show:
Welcome, <username>
💡 Bonus (optional but powerful):
Add multiple users (use dictionary)


dct = {"abc":"123","arc":"admin"}
attempts = 3
while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in dct:
        if dct[username] == password:
            print(f"Welcome, {username}")
            break
        else:
            print("Wrong password")
    else:
        print("User not found")
    attempts -= 1
    print(f"Remaining attempts: {attempts}")
if attempts == 0:
    print("Account locked")
"""

"""
🐞 Debugging Challenge 1: Infinite Loop
i = 1

while i <= 5:
    print(i)
❓ Problem:

This should print numbers 1–5, but it doesn’t stop.

👉 Fix it.


i = 1
while i<= 5:
    print(i)
    i+=1
"""

"""
🐞 Debugging Challenge 2: Wrong Sum
numbers = [1, 2, 3, 4, 5]
total = 0

for i in range(len(numbers)):
    total = i

print(total)
❓ Problem:

Expected output: 15
Actual output: 4

👉 Why? Fix it.

numbers = [1, 2, 3, 4, 5]
total = 0

for i in numbers:
    total += i

print(total)

"""

"""
🐞 Debugging Challenge 3: Login Bug
users = {"admin": "1234", "user": "pass"}

username = input("Username: ")
password = input("Password: ")

if username in users and password == users:
    print("Login successful")
else:
    print("Login failed")
❓ Problem:

Even correct credentials fail.

👉 Fix the logic.

users = {"admin": "1234", "user": "pass"}

username = input("Username: ")
password = input("Password: ")

if username in users:
    if users[username] == password:
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Login failed")
"""

"""
🐞 Debugging Challenge 4: Even Numbers
for i in range(1, 11):
    if i % 2 == 1:
        print(i)
❓ Problem:

It prints odd numbers, not even.

👉 Fix it.


for i in range(1, 11):
    if i % 2 == 0:
        print(i)
"""

"""
🐞 Multi-Bug Challenge 1: Broken Counter
count = 0

for i in range(1, 6):
    if i % 2 == 0:
        count =+ 1

print("Even numbers:", count)
❓ Expected:

Even numbers: 2

👉 Find and fix the bug(s)

count = 0

for i in range(1, 6):
    if i % 2 == 0:
        count += 1

print("Even numbers:", count)
"""
"""
🐞 Multi-Bug Challenge 2: Calculator Crash
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid")
❓ Problems:
Can crash
Missing validation

👉 Make it safe and robust


try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
except ValueError:
    print("Invalid number input")
    exit()
op = input("Enter operation (+, -, *, /): ")
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print(num1 / num2)
else:
    print("Invalid operator")
"""

"""
🐞 Multi-Bug Challenge 3: List Search
items = ["apple", "banana", "cherry"]

search = input("Enter item: ")

for i in items:
    if search == items:
        print("Found")
        break
else:
    print("Not found")
❓ Problems:
Always prints “Not found”

👉 Fix logic

items = ["apple", "banana", "cherry"]

search = input("Enter item: ")

for i in items:
    if search == i:
        print("Found")
        break
else:
    print("Not found")
"""


"""
🐞 Multi-Bug Challenge 4: Login System (Tricky)
users = {"admin": "1234", "user": "pass"}

attempts = 3

while attempts > 0:
    username = input("Username: ")
    password = input("Password: ")

    if username in users:
        if password == users[username]:
            print("Welcome")
        else:
            print("Wrong password")
    else:
        print("User not found")

    attempts -= 1

print("Account locked")
❓ Problems:
Even correct login still locks account
Logic flow issue

👉 Fix it properly

users = {"admin": "1234", "user": "pass"}

attempts = 3

while attempts > 0:
    username = input("Username: ")
    password = input("Password: ")
    if username in users:
        if password == users[username]:
            print("Welcome")
            break
        else:
            print("Wrong password")
    else:
        print("User not found")
    attempts -= 1
    if attempts == 0:
        print("Account locked")
"""

"""
🐞 Multi-Bug Challenge 5: Number Reversal
num = int(input("Enter number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse + digit
    num = num / 10

print("Reversed:", reverse)
❓ Problems:
Wrong result
Loop behaves incorrectly

👉 Fix it

num = int(input("Enter number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit 
    num = num // 10

print("Reversed:", reverse)
"""

"""
🔥 Hard Mode Debugging 1: Sneaky Average Bug
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

average = total / len(numbers) - 1

print("Average:", average)
❓ Expected:

30

👉 Something subtle is wrong.

numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

average = total / len(numbers)

print("Average:", average)

"""

"""
🔥 Hard Mode Debugging 2: Password Checker Trap
password = "python123"

user_input = input("Enter password: ")

if user_input == password:
    print("Access granted")

if user_input != password:
    print("Access denied")
else:
    print("Welcome")
❓ Problems:
Output is weird / duplicated
Logic structure is flawed

password = "python123"
user_input = input("Enter password: ")
if user_input == password:
    print("Access granted")
    print("Welcome")
else:
    print("Access denied")
"""

"""
🔥 Hard Mode Debugging 3: Loop + List Mutation (Classic Bug)
numbers = [1, 2, 3, 4, 5, 6]

for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)

print(numbers)
❓ Expected:

[1, 3, 5]

👉 Actual output is wrong. Why?

new_list = []
for num in numbers:
    if num % 2 != 0:
        new_list.append(num)
numbers = new_list
"""
"""
🔥 Hard Mode Debugging 4: Input Validation Gone Wrong
while True:
    num = input("Enter a number: ")
    if num.isdigit():
        num = int(num)
    else:
        print("Invalid input")
    if num > 10:
        print("Big number")
        break
❓ Problems:
Can crash
Logic flaw

while True:
    num = input("Enter a number: ")
    if not num.isdigit():
        print("Invalid input")
        continue
    num = int(num)
    if num > 10:
        print("Big number")
        break
"""

"""
🔥 Hard Mode Debugging 5: Function Logic Bug (Very Realistic)
def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient funds")
    if amount <= balance:
        balance -= amount
        print("Withdraw successful")
    return balance

balance = 100
balance = withdraw(balance, 150)
print(balance)
❓ Problems:
Logic allows incorrect behavior
Output is misleading

def withdraw(balance, amount):
    if amount <= 0:
        print("Invalid amount")
    elif amount > balance:
        print("Insufficient funds")
    else:
        balance -= amount
        print("Withdraw successful")
    return balance

"""

"""
🧠 OOP Practice Set (Progressive)
🟢 Task 1: Basic Class (Warm-up)

Create a class called Person.

Requirements:
Attributes:
name
age
Method:

introduce() → prints:

Hi, my name is <name> and I am <age> years old.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")
person = Person("Tunç",28)
person.introduce()

"""
"""
🟡 Task 2: Bank Account (Important)

Create a class BankAccount.

Requirements:
Attributes:
owner
balance (default = 0)
Methods:
deposit(amount)
withdraw(amount)
show_balance()
Rules:
❗ No negative deposits
❗ No withdrawing more than balance
Print messages for each action


class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance=balance
    def deposit(self,amount):
        if amount >= 0:
            self.balance += amount
            print(f"Deposited ${amount}")
        else:
            print(f"Deposit amount can not be negative")
    def withdraw(self, amount):
    if amount <= 0:
        print("Invalid amount")
    elif amount > self.balance:
        print("Insufficient funds")
    else:
        self.balance -= amount
        print(f"Withdrawn ${amount}")
    def show_balance(self):
        print(f"Current balance: {self.balance}")
"""

"""
🟠 Task 3: Student System

Create a class Student.

Requirements:
Attributes:
name
grades (list)
Methods:
add_grade(grade)
average() → returns average grade
is_passing() → returns True if avg ≥ 50

class Student:
    def __init__(self, name, grades=None):
        self.name = name
        self.grades = grades if grades is not None else []
    def add_grade(self,grade):
        self.grades.append(grade)
    def average(self):
        sum_grades=0
        for i in self.grades:
            sum_grades += i
        return sum(self.grades) / len(self.grades) if self.grades else 0
    def is_passing(self):
        return self.average() >= 50
"""

"""
🔴 Task 4: Simple Inventory System (Real OOP Thinking)

Create a class Product.

Requirements:
Attributes:
name
price
quantity
Methods:
buy(amount) → reduces quantity
restock(amount) → increases quantity
total_value() → price × quantity
Rules:
❗ Cannot buy more than available
❗ No negative values

class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def buy_amount(self,amount):
        if amount >= 0:
            if self.quantity >= amount:
                self.quantity -= amount
            else:
                print("Insufficient quantity")
        else:
            print("Amount must be positive")
    def restoke_amount(self,amount):
        if amount >= 0:
            self.quantity += amount
        else:
            print("Amount must be positive")
    def total_value(self):
        return self.price * self.quantity

"""

"""
🔥 Task 5 (Challenge): Multiple Objects Interaction

Create:

User class
BankAccount class
Requirements:
A User can have a BankAccount
User can:
deposit
withdraw
check balance

👉 This tests:

object interaction
real-world modeling

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
        else:
            self.balance += amount
            print(f"Deposited ${amount}")
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdraw amount")
        elif amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrawn ${amount}")
    def show_balance(self):
        print(f"Current balance: ${self.balance}")
class User:
    def __init__(self, name, bank_account):
        self.name = name
        self.bank_account = bank_account
    def deposit(self, amount):
        self.bank_account.deposit(amount)
    def withdraw(self, amount):
        self.bank_account.withdraw(amount)
    def show_balance(self):
        print(f"{self.name}'s account:")
        self.bank_account.show_balance()
account = BankAccount(1000)
user = User("Tunç", account)
user.deposit(500)
user.withdraw(200)
user.show_balance()
"""

"""
🧠 Linear Search Challenge
📌 Task

Write a program that searches for a number in a list using linear search (NOT in).

numbers = [7, 3, 9, 12, 5, 18, 21]
target = 18
steps = 0
for i in range(len(numbers)):
    steps+=1
    if numbers[i] == target:
        print(f"Found at index {i}")
        print(f"It took {steps} steps to find the number")
        break
else:
    print("Not found")
"""

