"""
1. 🔤 Basic Dictionary Access

Create a dictionary with 3 students and their scores.
Print the score of one specific student.

dct = {"Sal":86,"Harry":95,"Elliot":78}
print(f"Score of Sal is :{dct['Sal']}")
"""

"""
2. ➕ Add & Update

Create a dictionary of products and prices.

Add a new product
Update the price of an existing product

dct = {"Apple":0.5,"Banana":0.75,"Cherry":1}
dct["Watermelon"] = 1
dct["Apple"] = 0.6
for k,v in dct.items():
    print(k,v)
"""

"""
3. ❌ Remove Items

Given a dictionary of items, remove a specific key.
Also try removing the last inserted item.

dct = {"a":1,"b":2,"c":3,"d":4,"e":5}
dct.pop("b")
print(dct)
dct.popitem()
print(dct)
"""

"""
4. 🔁 Loop Through Dictionary

Given a dictionary of names → ages, print:

all keys
all values
both key and value

dct = {"a":1,"b":2,"c":3}
for i in dct.keys():
    print(i)
for i in dct.values():
    print(i)
for k,v in dct.items():
    print(k,v)
"""

"""
5. 🔍 Check Key Exists

Ask the user for a name.
Check if that name exists in a dictionary and print the result.

name = input("Enter a name")
dct = {"Alice":1,"Margot":2,"Denice":3}
if name in dct.keys():
    print(f"{name} is in the list")
else:
    print(f"{name} is not in the list")
"""

"""
6. 🔢 Count Frequency

Given a list:

[1, 2, 2, 3, 3, 3, 4]

Create a dictionary that counts how many times each number appears.

lst = [1, 2, 2, 3, 3, 3, 4]
dct = {}
for i in lst:
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1
print(dct)
"""

"""
7. 🔤 Word Counter

Take a sentence and count how many times each word appears.
Store the result in a dictionary.

sentence = input("Enter a sentence: ").split(" ")
dct = {}
for i in sentence:
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1
print(dct)
"""

"""
8. 📊 Find Max Value

Given a dictionary of students and scores, find the student with the highest score.

dct = {"Sally":70,"Mark":35,"Sam":50}
max_student = None
max_score = 0
for k, v in dct.items():
    if v > max_score:
        max_score = v
        max_student = k
print(max_student, max_score)
"""

"""
9. 🔄 Swap Keys and Values

Given a dictionary:

{"a": 1, "b": 2, "c": 3}

Create a new dictionary where keys and values are swapped.

dct = {"a": 1, "b": 2, "c": 3}
dct_2 = {}
for k,v in dct.items():
    dct_2[v] = k
print(dct_2)
"""

"""
10. 🧠 Merge Dictionaries

Given two dictionaries:

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

Merge them into one.
If a key exists in both, add the values together.

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3 = {}
for k in d1:
    if k in d2:
        d3[k] = d1[k] + d2[k]
    else:
        d3[k] = d1[k]
for k in d2:
    if k not in d3:
        d3[k] = d2[k]
print(d3)
"""

"""
📞 Mini Phonebook System — Step-by-Step Ideas
🧠 Step 1: Decide what you are building

You are creating a system that:

stores contacts
finds contacts
removes contacts
shows all contacts

👉 Think of it like a small “phone app inside the console”
"""
"""
🗂 Step 2: Decide your data structure

Ask yourself:

What links a name to a phone number?

👉 You should use a structure where:

each name maps to one or more numbers

Think:

“key → value system”
"""
"""
🧱 Step 3: Define the features (menu)

Your program should repeat forever and offer choices like:

Add contact
Search contact
Delete contact
Show all contacts
Exit program

👉 This is your main control system

class Contact:
    def __init__(self,name,phone_number):
        self.name = name
        self.phone_number = phone_number
class Phonebook:
    def __init__(self):
        self.dct={}
    def add_contact(self,contact):
        if contact.name in self.dct:
            print("Cannot add duplicate names")
        else:
            self.dct[contact.name] = contact.phone_number
    def search_contact_by_name(self,name):
        if name in self.dct:
            print(f"Name :{name} Number: {self.dct[name]}")
        else:
            print(f"{name} doesn't exist")
    def delete_contact_by_name(self,name):
        if name in self.dct:
            self.dct.pop(name)
        else:
            print(f"{name} doesn't exist")
    def show_all_contacts(self):
        for k,v in self.dct.items():
            print(f"Name:{k} Number:{v}")
c1 = Contact("Sam",123)
print(c1.name)
print(c1.phone_number)
pb = Phonebook()
pb.add_contact(c1)
"""

"""
🧱 1. Person System
Person class
attributes: name, age
method: introduce themselves

👉 Focus: basic class + attributes


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hi my name is {self.name} i am {self.age}")

"""

"""
🐶 2. Animal Sounds
Animal class
Dog, Cat classes

Each has:

a sound method

👉 Focus: inheritance + simple polymorphism

class Animal:
    def __init__(self,type):
        self.type = type
    def make_sound(self):
        print(f"{self.type} is making noises")
class Dog(Animal):
    def __init__(self,breed):
        super().__init__("Dog")
        self.breed = breed
    def make_sound(self):
        print(f"{self.breed} dog is barking")
class Cat(Animal):
    def __init__(self,breed):
        super().__init__("Cat")
        self.breed = breed
    def make_sound(self):
        print(f"{self.breed} cat is making noise")
        
a = Animal("Wolf")
a.make_sound()
d = Dog("Labrador")
d.make_sound()
c = Cat("Orange")
c.make_sound()
"""

"""
🚗 3. Car System
Car class
attributes: brand, speed

Methods:

accelerate
brake

👉 Focus: object state changes

class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed
    def accelerate(self, value):
        if value > 0:
            self.speed += value
    def brake(self, value):
        if value > 0:
            self.speed -= value
            if self.speed < 0:
                self.speed = 0
"""

"""
📚 4. Book System
Book class

Attributes:

title, author

Method:

show info

👉 Focus: clean object structure

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def show_info(self):
        print(f"{self.title} written by {self.author}")
"""

"""
🧮 5. Calculator Class
Calculator class

Methods:

add, subtract, multiply, divide

👉 Focus: methods vs logic

class Calculator:
    def add(self, *numbers):
        return sum(numbers)
    def subtract(self, first, *numbers):
        result = first
        for num in numbers:
            result -= num
        return result
    def multiply(self, *numbers):
        result = 1
        for num in numbers:
            result *= num
        return result
    def divide(self, a, b):
        if b == 0:
            print("Cannot divide by zero")
            return None
        return a / b
"""

"""
🏦 6. Simple Wallet
Wallet class
balance

Methods:

add money
spend money

👉 Focus: state updates safely

class Wallet:
    def __init__(self,balance):
        self.balance = balance
    def add_money(self,amount):
        if not amount < 0:
            self.balance += amount
        else:
            print("Amount cant be negative")
    def spend_money(self,amount):
        if not amount < 0:
            self.balance -= amount
        else:
            print("Amount cant be negative")

"""

"""
🎮 7. Game Character
Character class
health, damage

Methods:

take damage
heal

👉 Focus: object state mutation

class Character:
    def __init__(self,health,damage):
        self.health = health
        self.damage = damage
    def take_damage(self,value):
        if not value < 0:
            self.health -= value
        elif (self.health - value) < 0:
            print("Health cant be negative")
        else:
            print("Value cant be negative")
    def heal(self,value):
        if not value < 0:
            self.health += value
        else:
            print("Value cant be negative")
"""

"""
📝 8. To-Do Task
Task class
name, done/not done

Method:

mark complete

👉 Focus: boolean state

class Task:
    def __init__(self, name):
        self.name = name
        self.is_done = False

    def mark_complete(self):
        self.is_done = True

    def show_status(self):
        status = "Done" if self.is_done else "Not Done"
        print(f"{self.name}: {status}")
"""

"""
🔢 9. Counter
Counter class
number

Methods:

increment
decrement
reset

👉 Focus: simple state control

class Counter:
    def __init__(self, number=0):
        self.number = number
    def increment(self):
        self.number += 1
    def decrement(self):
        self.number -= 1
    def reset(self):
        self.number = 0
"""

"""
🧑‍🎓 10. Student (Very Basic Version)
Student class
name, grade

Method:

show info

👉 Focus: simple object design (no lists yet)

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def show_info(self):
        print(f"{self.name} has grade {self.grade}")
"""


"""
🧠 1. Attribute Not Updating
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        value += 1

c = Counter()
c.increment()
print(c.value)
👉 Why doesn’t the value change?

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1 #Added self keyword

c = Counter()
c.increment()
print(c.value)
"""

"""
🧠 2. Wrong Object Used
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Alice")
p2 = Person("Bob")

print(p1.name)
p2.name = "Charlie"
print(p1.name)

👉 Why doesn’t p1 change?

class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Alice")
p2 = Person("Bob")

print(p1.name)
p2.name = "Charlie" #Because its not modified
print(p1.name)
"""

"""
🧠 3. List vs Integer Mistake
class Wallet:
    def __init__(self):
        self.balance = [100]

    def spend(self, amount):
        self.balance -= amount

w = Wallet()
w.spend(20)
print(w.balance)

👉 What error happens and why?

class Wallet:
    def __init__(self):
        self.balance = [100] #This is a list which throws type error because code tries to subtract an int type from a list type

    def spend(self, amount):
        self.balance -= amount #Either change self.balance[0] or make self.balance an integer

w = Wallet()
w.spend(20)
print(w.balance)
"""

"""
🧠 4. Missing self
class Dog:
    def __init__(self, name):
        self.name = name

    def bark():
        print(f"{self.name} is barking")

d = Dog("Max")
d.bark()

👉 Why does this fail?

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self): #There is no self keyword here so code cant refer to self.name attribute
        print(f"{self.name} is barking")

d = Dog("Max")
d.bark()
"""

"""
🧠 5. Shared Mutable Bug
class Student:
    def __init__(self, name, grades=[]): #That list is created once and shared by ALL objects.So: s1.grades.append(100) affects s2.grades too
        self.name = name
        self.grades = grades

s1 = Student("A")
s2 = Student("B")

s1.grades.append(100)

print(s1.grades)
print(s2.grades)

👉 Why does s2 also change?
"""

"""
🧠 6. Wrong Return Logic
class Calculator:
    def add(self, a, b):
        result = a + b

c = Calculator()
print(c.add(2, 3))

👉 Why does it print None?

class Calculator:
    def add(self, a, b):
        result = a + b
        return result #Missing return

c = Calculator()
print(c.add(2, 3))
"""

"""
🧠 7. Incorrect Comparison
class Car:
    def __init__(self, speed):
        self.speed = speed

    def is_fast(self):
        if self.speed > "100":
            return True
        return False

c = Car(120)
print(c.is_fast())

👉 What’s wrong here?

class Car:
    def __init__(self, speed):
        self.speed = speed

    def is_fast(self):
        if self.speed > 100: #Cant compare string with integer remove make "100" int
            return True
        return False

c = Car(120)
print(c.is_fast())

"""

"""
🧠 8. Object vs String Confusion
class Student:
    def __init__(self, name):
        self.name = name

class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student(self, name):
        if name in self.students:
            return name

s = School()
s.add_student(Student("Ali"))

print(s.find_student("Ali"))

👉 Why doesn’t it find the student?

class Student:
    def __init__(self, name):
        self.name = name

class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student) 

    def find_student(self, name): 
        if name in self.students: # for name in self.students: if student.name == name return student 
            return name

s = School()
s.add_student(Student("Ali"))

print(s.find_student("Ali"))
"""

"""
🧠 9. Overwriting Attribute
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = amount

acc = BankAccount(100)
acc.deposit(50)
print(acc.balance)

👉 Why is balance wrong?

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = amount #Missing += operator instead of assigning it use +=

acc = BankAccount(100)
acc.deposit(50)
print(acc.balance)

"""

"""
🧠 10. Infinite Growth Bug
class Numbers:
    def __init__(self):
        self.nums = [1, 2, 3]

    def add_numbers(self):
        for n in self.nums:
            self.nums.append(n)

obj = Numbers()
obj.add_numbers()
print(obj.nums)

👉 What goes wrong here?

class Numbers:
    def __init__(self):
        self.nums = [1, 2, 3]

    def add_numbers(self):
        for n in self.nums:
            self.nums.append(n) #For each iteration code appends more numbers to the list so iteration never ends

obj = Numbers()
obj.add_numbers()
print(obj.nums)
"""

"""
🧠 1. Hidden Shared State (Tricky)
class Inventory:
    items = []

    def add_item(self, item):
        self.items.append(item)

inv1 = Inventory()
inv2 = Inventory()

inv1.add_item("Sword")

print(inv1.items)
print(inv2.items)

👉 Why does inv2 also have "Sword"?

class Inventory:
    items = [] #Because this list is a class variable meaning shared across all instances of class

    def add_item(self, item):
        self.items.append(item)

inv1 = Inventory()
inv2 = Inventory()

inv1.add_item("Sword")

print(inv1.items)
print(inv2.items)
"""

"""
🧠 2. Object Comparison Trap
class User:
    def __init__(self, name):
        self.name = name

u1 = User("Ali")
u2 = User("Ali")

print(u1 == u2)

👉 Why is this False even though names are the same?

class User:
    def __init__(self, name):
        self.name = name

u1 = User("Ali")
u2 = User("Ali")

print(u1 == u2) #This line doesnt compare names.It compares 2 memory location with the same name attribute

"""

"""
🧠 3. Method Not Affecting Original Object
class Wallet:
    def __init__(self, balance):
        self.balance = balance

def spend(wallet, amount):
    wallet = Wallet(wallet.balance - amount) #Code must modify wallet.balance directly

w = Wallet(100)
spend(w, 30)

print(w.balance)

👉 Why does balance not change?
"""

"""
🧠 4. Mutable Argument Mutation
class Data:
    def __init__(self, values):
        self.values = values

    def add_value(self, value):
        new_values = self.values
        new_values.append(value)

d1 = Data([1, 2])
d2 = d1

d1.add_value(3)

print(d2.values)

👉 Why does modifying d1 affect d2?

class Data:
    def __init__(self, values):
        self.values = values

    def add_value(self, value):
        new_values = self.values
        new_values.append(value)

d1 = Data([1, 2]) 
d2 = d1 #d2 and d1 referencing the same object so if d1 changes d2 also changes.

d1.add_value(3)

print(d2.values)

"""








