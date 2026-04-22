"""
🧠 String Practice Set (10 Questions)
🟢 1. Reverse a String

Ask the user for a word and print it reversed.

🚫 Don’t use [::-1] (use a loop)

word = input("Enter a word: ")
word_1 = ""
length = len(word)-1
while length >= 0:
    word_1 += word[length]
    length -= 1
print(word_1)

"""


"""
🟢 2. Count Vowels

Ask the user for a string and count how many vowels it has.

👉 vowels = a, e, i, o, u

count = 0
vowels = ["a","e","i","o","u"]
word = input("Enter a word: ")
for i in word:
    if i in vowels:
        count += 1
print(count)

"""

"""
🟡 3. Check Palindrome

Ask the user for a word and check if it is a palindrome.

👉 Example:
madam → True
hello → False

word = input("Enter a word: ")
print("True" if word[::-1] == word else "False")
"""

"""
🟡 4. Remove Spaces

Ask the user for a sentence and remove all spaces.

👉 "hello world" → "helloworld"

word = input("Enter a word: ")
word_2 = ""
for i in words:
    if i != " ":
        word_2 += i
"""

"""
🟡 5. Count Characters

Ask the user for a string and print:

number of letters
number of digits

word=input("Enter a word: ")
count_letter = 0
count_digit = 0
for i in word:
    if i.isalpha():
        count_letter += 1
    elif i.isdigit():
        count_digit += 1
    else:
        continue
print(f"Letters:{count_letter} Digits:{count_digit}")

"""

"""
🟠 6. Find Largest Word

Ask the user for a sentence and print the longest word.

sentence = input("Enter a sentence: ")
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word
print(longest)
"""

"""
🟠 7. Replace Characters

Ask the user for a string and:

replace all "a" with "@"
replace all "e" with "3"

word = input("Enter a string: ")
word_2 = ""
for i in range(len(word)):
    if word[i] != "a" and word[i] != "e":
        word_2 += word[i]
    elif word[i] == "a":
        word_2 += "@"
    elif word[i] == "e":
        word_2 += "3"
print(word_2)


"""

"""
🔴 8. Character Frequency

Ask the user for a string and print how many times each character appears.

👉 Example:

hello
h:1
e:1
l:2
o:1

word = input("Enter a string: ")
dct={}
for i in word:
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1
print(dct)

"""

"""
🔴 9. First Non-Repeating Character

Find the first character that appears only once.

👉 Example:

swiss → w

word = input("Enter a string: ")
dct = {}
for char in word:
    if char in dct:
        dct[char] += 1
    else:
        dct[char] = 1
for char in word:
    if dct[char] == 1:
        print(char)
        break
"""


"""
🔥 10. String Compression (Challenge)

Compress a string like this:

👉 Input:

aaabbc

👉 Output:

a3b2c1

word = "aaabbc"
dct = {}
for i in word:
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1
word_1 = ""
for k,v in dct.items():
    word_1 += k
    word_1 += str(v)
print(word_1)
"""

"""
🧠 List Practice Set (10 Questions)
🟢 1. Sum of List

Create a list of numbers and calculate the sum using a loop.

🚫 Don’t use sum()

lst = [1,2,3,4,5,6,7,8,9,10]
sum_of_lst = 0
for i in lst:
    sum_of_lst += i
print(sum_of_lst)
"""

"""
🟢 2. Find Maximum

Find the largest number in a list.

🚫 Don’t use max()

lst = [1,2,3,4,15,6,7,8,9,10]
maxi = lst[0]
for i in lst:
    if i > maxi:
        maxi = i
print(maxi)

"""

"""
🟢 3. Count Occurrences

Ask user for a number and count how many times it appears in a list.

lst = [1,1,2,2,3,3,3,3,5,5,15,15,0,2]
number = int(input("Enter a number :"))
count_num = 0
for i in lst:
    if number == i:
        count_num +=1
print(count_num)

"""

"""
🟡 4. Reverse a List

Reverse a list manually using a loop.

🚫 Don’t use [::-1]

lst = [1,2,3,4,5,"abc",True]
lst_2 = []
length = len(lst)-1
while length>=0:
    lst_2.append(lst[length])
    length -= 1
print(lst_2)

"""

"""
🟡 5. Remove Duplicates

Remove duplicate elements from a list.

👉 Keep order
🚫 Don’t use set()

lst = [1,2,1,2,4,3,4,3,1,4]
result = []
for i in lst:
    if i not in result:
        result.append(i)
print(result)
"""

"""
🟡 6. Second Largest Number

Find the second largest number in a list.

🚫 Don’t sort the list

lst = [1,2,5,5,4,3]
first = second = float("-inf")
for i in lst:
    if i > first:
        second = first
        first = i
    elif i > second and i != first:
        second = i
print(second)

"""


"""
🟠 7. Merge Two Lists (Alternate)

Merge two lists like this:

[1,2,3], [4,5,6]

👉 Output:

[1,4,2,5,3,6]

lst_3 = []
lst_1 = [1,2,3]
lst_2 = [4,5,6]
for i in range(len(lst_1)):
    lst_3.append(lst_1[i])
    lst_3.append(lst_2[i])
print(lst_3)

"""

"""
🟠 8. Find Common Elements

Given two lists, find common elements.

👉 Example:

[1,2,3], [2,3,4] → [2,3]

lst_1 = [1,2,3]
lst_2 = [2,3,4]
lst_3 = []
for i in lst_1:
    if i in lst_2:
        lst_3.append(i)
print(lst_3)

"""

"""
🔴 9. Rotate List

Rotate a list to the right by 1.

[1,2,3,4] → [4,1,2,3]

lst=[1,2,3,4]
last = lst[len(lst)-1]
lst.insert(0,last)
lst.pop(len(lst)-1)
print(lst)
"""

"""
🔥 10. Sublist Check (Challenge)

Check if one list is a sublist of another.

👉 Example:

[1,2,3,4,5], [3,4] → True
[1,2,3], [2,4] → False

lst_1 = [1,2,3,4,5]
lst_2 = [3,4]
found = False
for i in range(len(lst_1) - len(lst_2) + 1):
    match = True
    for j in range(len(lst_2)):
        if lst_1[i + j] != lst_2[j]:
            match = False
            break
    if match:
        found = True
        break
print(found)
"""

"""
🧠 Binary Search Practice (10 Questions)
🟢 1. What must be true for binary search to work?

👉 Explain in your own words.

Binary search algorithm relies on the structure of the list that is implemented on.
If list is not sorted binary search wont work.
"""

"""
🟢 2. What is the time complexity of binary search?

👉 And why is it faster than linear search?

Time complexity of binary search is O(log n).
Time complexity of linear search is O(n).
Thus linear search is slower.
Since linear search algorithm traverses each element in the list it takes O(n) time worst case.
But binary search discards half of list in each iteration thus it is better to use.
"""

"""
🟡 3. What happens if the list is NOT sorted?

👉 Will binary search still work? Why or why not?

It won't work because i need to be able to find middle value,least and max value.
If list is not sorted i could possibly discard the value im searching for.
If a contact numbers book wasn't sorted alphebatically i would have to search every
page from beginning to end.
"""

"""
🟡 4. Find the middle index

Given:

left = 0
right = 9

👉 What is mid?

left = 0
right = 9
mid = (left+right) // 2
print(mid)
mid value is 4 which is the index number
"""

"""
🟡 5. First Step Simulation

Given:

[2, 4, 6, 8, 10, 12]
target = 10

👉 What is the first mid value checked?

lst = [2, 4, 6, 8, 10, 12]
left = 0
right = len(lst)-1
target = 10
mid = (left+right) // 2
print(lst[mid])
mid index = 2
mid value = 6
6 is the mid value in first iteration
"""

"""
🟠 6. Trace the Algorithm

Given:

[1, 3, 5, 7, 9]
target = 7

👉 List each step (mid values + direction taken)

[1, 3, 5, 7, 9]
target = 7
First iteration:
left = 0, right = 4
mid = 2 → value = 5
7 > 5 → go right
discard left side

Second iteration:
left = 3, right = 4
mid = 3 → value = 7
Found
"""


"""
🟠 7. Why do we update only one side (left OR right)?

👉 Explain why we don’t search both sides.

Since i know its not the middle value and list is sorted.
Target has to be in only one side of the list.
"""

"""
🔴 8. Write pseudocode

Write binary search in plain English steps (no Python).

i have a list = [1,2,3,4,5,6,7,8,9,10]
and target is 9
first i find the left and right values
then calculate middle
if target equals middle return true
else if target is bigger than middle, discard left side
else if target is lesser than middle, discard right side
continue to repeat while left <= right
return -1 if not found
"""

"""
🔴 9. Bug Detection

What is wrong with this logic?

if target > mid:
    right = mid
else:
    left = mid

if target is bigger than mid it means target is on the right side of the list
but in code right is equal to mid when it should have been left.

"""

"""
🔥 10. Real Problem

Why is binary search NOT always the best choice, even though it is fast?

👉 Give at least 2 reasons.

From what i understand dictionary look up time is O(1) which is faster than binary search.
For binary search to work i must sort the list which is not optimal.
"""

"""
def binary_search(lst,target):
    left = 0
    right = len(lst)-1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] >= target:
            left = mid +1
        else:
            right = mid -1 
    return -1
"""

"""
🧠 *args and **kwargs Practice (10 Questions)
🟢 1. Basic *args Sum

Write a function that takes any number of numbers and returns their sum.

👉 Example:

add(1, 2, 3, 4) → 10

def func(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(func(1,2,3,4))
"""

"""
🟢 2. Print All Arguments

Write a function that prints all values passed using *args
def func(*args):
    for arg in args:
        print(arg)
func(1,2,3,4,5,"num")
"""

"""
🟢 3. Count Arguments

Write a function that returns how many arguments were passed using *args.
def func(*args):
    arguments = 0
    for arg in args:
        arguments += 1
    return arguments
print(func(5,6,7,True))
"""

"""
🟡 4. Find Maximum Using *args

👉 Do NOT use max().

Return the largest number from arguments. 

def func(*args):
    maxi = args[0]
    for i in args:
        if i > maxi:
            maxi = i
    return maxi
print(func(True,1,10,3,4,5))

"""

"""
🟡 5. Multiply All Arguments

Multiply all numbers passed via *args.

def func(*args):
    multiple = 1
    for arg in args:
        multiple *= arg
    return multiple
print(func(1,2,3,4,5))

"""

"""
🟡 6. Keyword Arguments Printer

Write a function that prints all key-value pairs from **kwargs.

👉 Example:

name="Ali", age=20

def func(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} = {v}")
print(func(name="Ali",age=20))

"""

"""
🟡 7. Profile Builder

Create a function that accepts:

name (positional)
**kwargs (extra info)

Print everything nicely.

def func(name, **kwargs):
    print("Name:", name)
    for k, v in kwargs.items():
        print(f"{k} = {v}")
func(name = "Tunç",age=28,phone="123-123")

"""

"""
🟠 8. Default + *args Mix

Write a function:

def greet(greeting, *args)

Print:

Hello Ali
Hello John

def func(greeting,*args):
    for arg in args:
        print(greeting,arg)
func("Hello","Ali","John")

"""

"""
🟠 9. Combine *args and **kwargs

Write a function that accepts both and prints them separately.
def func(greeting, *args, bye, **kwargs):
    for arg in args:
        print(greeting, arg)
    print(bye)
    for k, v in kwargs.items():
        print(k, v)
func("Hi","Ali","John","Alice",bye="Goodbye",profession="dentist",experience=5,age=20)
"""


"""
🔴 10. Flexible Calculator

Create a function:

def calculator(operation, *args)
operation = "add", "mul"
*args = numbers

👉 Example:

calculator("add", 1, 2, 3)
→ 6

def calculator(op,*args):
    if op == "add":
        total = 0
        for arg in args:
            total += arg
        return total
    elif op == "mul":
        total = 1
        for arg in args:
            total *= arg
        return total
print(calculator("add",1,2,3,4))
print(calculator("mul",1,2,3,4,5))
"""

"""
🟢 1. Write to a File

Create a file notes.txt and write:

Hello Python

👉 Then close it properly using with.

with open("Practice\\Day_2\\file.txt" , "x") as f:
    f.write("Hello World")
"""

"""
🟢 2. Read Entire File

Read notes.txt and print its full content.

with open("Practice\\Day_2\\file.txt") as f:
    print(f.read())
"""

"""
🟢 3. Read File Line by Line

Print each line separately.

👉 Hint: use a loop.

with open("Practice\\Day_2\\file.txt") as f:
    for i in f:
        print(i)
"""

"""
🟢 4. Count Lines

Count how many lines are in a file.

lines = 0
with open("Practice\\Day_2\\file.txt") as f:
    for i in f:
        lines += 1
print(lines)
"""

"""
🟢 5. Count Words

Count total words in a file.

👉 Hint: use .split()

total = 0
with open("Practice\\Day_2\\file.txt") as f:
    for i in f:
        for j in i.split():
            total += 1
print(total)
"""

"""
🟡 6. Count Characters

Count total characters (including spaces).

total = 0
with open("Practice\\Day_2\\file.txt") as f:
    for i in f:
        for j in i:
            total += 1
print(total)

"""

"""
🟡 7. Find Specific Word Occurrences

Count how many times the word "Python" appears in a file.

👉 Case-insensitive.

with open("Practice\\Day_2\\file2.txt" , "x") as f:
    f.write("Python is a very Pythonic language.Python")
count = 0
target = "python"
with open("Practice\\Day_2\\file2.txt") as f:
    for line in f:
        for word in line.split():
            if word.lower() == target:
                count += 1
print(count)
"""

"""
🟡 8. Append Data to File

A file already has content.

👉 Add new text without deleting old content.

with open("Practice\\Day_2\\file2.txt", "a") as f:
    f.write("is a good language")

with open("Practice\\Day_2\\file2.txt") as f:
    print(f.read())
"""

"""
🟠 9. Copy File Content

Copy everything from file1.txt → file2.txt

with open("Practice\\Day_2\\file.txt", "r") as f1, open("Practice\\Day_2\\file2.txt", "w") as f2:
    for line in f1:
        f2.write(line)

with open("Practice\\Day_2\\file.txt") as f:
    for i in f:
        print(i)
"""
"""
🏦 1. BANK SYSTEM (Broken)
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance + amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")
        self.balance -= amount
        print("Withdrawn:", amount)

acc = BankAccount("Ali", 100)

acc.deposit(50)
acc.withdraw(200)
print(acc.balance)


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount #Missing += operator
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance -= amount #Missing edge case
            print("Withdrawn:", amount)

acc = BankAccount("Ali", 100)

acc.deposit(50)
acc.withdraw(200)
print(acc.balance)
"""

"""
🔐 2. LOGIN SYSTEM (Broken Security Logic)
users = {
    "admin": "1234",
    "user": "pass"
}

username = input("Username: ")
password = input("Password: ")

if username in users or users[username] == password:
    print("Login success")
else:
    print("Login failed")

users = {
    "admin": "1234",
    "user": "pass"
}

username = input("Username: ")
password = input("Password: ")

if username in users and users[username] == password: #Wrong pairs of username and pwd allows access replaced or with and
    print("Login success")
else:
    print("Login failed")

"""


"""
🔐 1. USER REGISTRATION SYSTEM (BROKEN BACKEND LOGIC)
users = {}

def register(username, password):
    if username in users:
        print("User already exists")

    users[username] = password
    print("User registered")

register("admin", "1234")
register("admin", "0000")
print(users)

users = {}

def register(username, password):
    if username in users:
        print("User already exists")
        return
    users[username] = password
    print("User registered")
register("admin", "1234")
register("admin", "0000")
print(users)
"""

"""
💳 2. SIMPLE PAYMENT SYSTEM (BROKEN)
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

def transfer(sender, receiver, amount):
    sender.balance -= amount
    receiver.balance += amount
    print("Transfer complete")

a = Account("Ali", 100)
b = Account("Bob", 50)

transfer(a, b, 120)
print(a.balance, b.balance)

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

def transfer(sender, receiver, amount):
    if amount <= 0:
        print("Invalid amount")
        return
    if sender.balance < amount:
        print("Insufficient funds")
        return
    sender.balance -= amount
    receiver.balance += amount
    print("Transfer complete")
a = Account("Ali", 100)
b = Account("Bob", 50)
transfer(a, b, 120)
print(a.balance, b.balance)
"""

"""
📦 3. PRODUCT INVENTORY API (BROKEN)
inventory = {
    "apple": 10,
    "banana": 5
}

def buy_item(item, quantity):
    inventory[item] -= quantity
    print("Purchased:", item, quantity)

buy_item("apple", 3)
buy_item("banana", 10)
buy_item("orange", 1)
print(inventory)

inventory = {
    "apple": 10,
    "banana": 5
}

def buy_item(item, quantity):
    if quantity <= 0:
        print("Invalid quantity")
        return
    if item not in inventory:
        print("Item not found")
        return
    if inventory[item] < quantity:
        print("Not enough stock")
        return
    inventory[item] -= quantity
    print("Purchased:", item, quantity)
buy_item("apple", 3)
buy_item("banana", 10)
buy_item("orange", 1)
print(inventory)
"""

