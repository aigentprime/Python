"""
🟢 Exercise 1: Write JSON to a file

👉 Task:

Create a dictionary like:
name: "Ali"
age: 20
Save it into a file called data.json

👉 Questions to think about:

Which module do you need?
Which function writes JSON to a file?

import json
FILE = "Practice\\Day_4\\file.json"
dct = {"Ali":20}
def write_data():
    json_str = json.dumps(dct,indent=4) --> Convert dictionary to json
    with open(FILE,"w") as f:
        f.write(json_str)
write_data()
"""

"""
🟢 Exercise 2: Read JSON from a file

👉 Task:

Read data.json
Print the name and age

👉 Goal:
Understand how to load JSON back into Python

import json
FILE = "Practice\\Day_4\\file.json"
def read_data():
    with open(FILE,"r") as f:
        data = json.load(f) # --> Convert json to dictionary
        for k,v in data.items():
            print(k,v)
read_data()
"""

"""
🟡 Exercise 3: Modify JSON data

👉 Task:

Load the file
Change age to 25
Save it again

👉 Key idea:
You’re editing data, not just reading it

import json

FILE = "Practice\\Day_4\\file.json"

dct = {"Samuel":20}
with open(FILE,"w") as f:
    json.dump(dct,f)
with open(FILE,"r") as f:
    data = json.load(f)
data["Samuel"] = 25
with open(FILE,"w") as f:
    json.dump(data,f)
with open(FILE,"r") as f:
    data = json.load(f)
    print(data)
"""

"""
🟡 Exercise 4: Store multiple users

👉 Task:
Store this:

A → 1234
B → 5678

👉 Question:

Should you use a list or dictionary?

👉 Then:

Save it to JSON
Print all users

import json
FILE = "Practice\\Day_4\\file.json"
dct={"A":1234,"B":5678}
with open(FILE,"w") as f:
    json.dump(dct,f)
with open(FILE,"r") as f:
    data = json.load(f)
    for k,v in data.items():
        print(k,v)

"""

"""
🟡 Exercise 5: Add new data from user input

👉 Task:

Ask user for name and password
Add it to existing data
Save it

👉 This is basically your password manager starting point 👀

import json
import os

FILE = "Practice\\Day_4\\file.json"
if os.path.exists(FILE):
    with open(FILE, "r") as f:
        data = json.load(f)
else:
    data = {}
key = input("Enter name: ")
value = input("Enter password: ")
data[key] = value
with open(FILE, "w") as f:
    json.dump(data, f, indent=4)
for k,v in data.items():
    print(k,v)
"""

"""
🟠 Exercise 6: Handle missing file

👉 Problem:
What if data.json does NOT exist?

👉 Task:

Prevent your program from crashing
Start with empty data instead

FILE = "Practice\\Day_4\\file.json"
try:
    with open(FILE,"r") as f:
        content = f.read()
        print(content)
        print(f"{FILE} exists")
except FileNotFoundError:
    print(f"{FILE} doesn't exists")
    print(f"Creating file at {FILE}")
    with open(FILE, "w") as f:
        json.dump({}, f)


"""

"""
🟠 Exercise 7: Search in JSON

👉 Task:

Ask user for a name
If it exists → print password
If not → print “Not found

import json
import os
FILE = "Practice\\Day_4\\file.json"
if os.path.exists(FILE):
    with open(FILE, "r") as f:
        data = json.load(f)
else:
    data = {}
name = input("Enter a name: ")
if name in data:
    print(f"{name} exists with {data[name]} value")
else:
    print("Not found")
"""

"""
 🧠 Important Concepts You Should Learn

By the end, you should understand:

json.dump() → save data
json.load() → read data
dictionaries ↔ JSON conversion
file modes ("r", "w")
"""
















