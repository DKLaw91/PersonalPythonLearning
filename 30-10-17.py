https://www.learnpython.org/en/Exception_Handling
__________________________________________-
def do_stuff_with_number(n):
  print(n)
  
the_list=(1,2,3,4,5)

for i in range(20):
  try:
    do_stuff_with_number(the_list[i])
  except IndexError: # Raised when accessing a non-existing index of a list
    print("No Number Entered")
print()

actor= {"name": "Chris Hemsworth", "rank": "Legend"}

#Function to modify, should return the last name of the actor - think back to previous lessons for how to get it
def get_last_name():
    lastname=(actor["name"].split(" ")[1])
    return lastname

#Test code
get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s." % get_last_name())
___________________________________________________---
https://www.learnpython.org/en/Sets
  
print(set("My name is Jeff and Jeff is my name".split()))
print()

a=set(["Jeff", "Jeffery", "Jeffald"])
print(a)
b=set(["Jeff", "Jeffaldine"])
print(b)
print()

print(a.intersection(b))
print(b.intersection(a))
print()

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
print()

print(a.difference(b))
print(b.difference(a))
print()

print(a.union(b))
print()

#In the exercise below, use the given lists to print out a set containing all the participants from event A which did not attend event B.

c = set(["Jake", "John", "Eric"])
d = set(["John", "Jill"])
print(c.difference(d))
___________________________________________-
https://www.learnpython.org/en/Serialization
  
import json

json_string=json.dumps([1,2,3,"a","b", "c"])
print(json_string) # Creates JSON Data Structure
print()
print(json.loads(json_string)) # Reverts back to standard Data Structure
print()

import pickle

pickled_string=pickle.dumps([1,2,3,"a","b","c"])
print(pickled_string)
print(pickle.loads(pickled_string))
print()

import json

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
  salaries_json[name]=salary
  return salaries_json

# test code
salaries = {"Alfred" : 300, "Jane" : 400 }
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = new_salaries
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])
_____________________________________
https://www.learnpython.org/en/Partial_functions
  
from functools import partial

def multiply(x,y):
  return x*y

print(multiply(2,4))

dbl=partial(multiply,2)
print(dbl(4))

tpl=partial(multiply,3)
print(tpl(4))
print()

#Following is the exercise, function provided:
from functools import partial
def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x
#Enter your code here to create and print with your partial function
answer=partial(func, 8, 4, 2)
print(answer(12))
_____________________________________-
https://www.learnpython.org/en/Code_Introspection
  
# Define the Vehicle class.
class Vehicle:
    name = "Fermi"
    kind = "car"
    color = "Red"
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# Print a list of all attributes of the Vehicle class.
# Your code goes here

for i in dir(Vehicle):
  print(i)
  





