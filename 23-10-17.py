https://www.learnpython.org/en/Classes_and_Objects
____________________________________________________
class myClass:
  variable="blah"
  
  def function(self):
    print("This is a message inside the class.")
    
myobjectx=myClass() # Class is assignable to Objects

print(myobjectx.variable) # To access variable within Class

print(myobjectx.function()) # To access function within Class

print()

myobjecty=myClass() # Assigns variable & function from Class but is seperate to myobjectx

myobjecty.variable="Jeffald" 
myobjectx.variable="Jeff" 
# Objects are seperate from one another & are not affected by altering the other - same for Class

print(myobjecty.variable)
print(myobjectx.variable)
print(myClass.variable)
print()

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1=Vehicle()
car1.name="Fer"
car1.color="Red"
car1.value=60000.00

car2=Vehicle()
car2.name="Jump"
car2.color="Blue"
car2.value=10000.00


# test code
print(car1.description())
print()
print(car2.description())
_______________________________________________________________
https://www.learnpython.org/en/Dictionaries
 
phonebook={}
phonebook["John"]=914065212 # Accepts max of 9 digits!
phonebook["Jeff"]=87405683
phonebook["Jeffald"]=745450808
print(phonebook)
print()

# Alternative method of entry
phonebook= {
  "Maloy" : 966241398, # Don't forget Comma!
  "'Cyril'" : 761747235,
  "Magoo" : 866408643,
  "John" : 914065212,
  "Jeff" : 87405683,
  "Jeffald" : 745450808
}
print(phonebook)
print()

for name, number in phonebook.items():
  print("Phone number of " + name + " is: 07" + str(number))
  print()

del phonebook["John"]
phonebook.pop("Jeffald") # Also deletes dictionary item

print(phonebook)
print()

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# write your code here
phonebook["Jake"]=938273443 # This is how to add to Dictionary
phonebook.pop("Jill")

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")
_____________________________________________________________
https://www.learnpython.org/en/Modules_and_Packages

import urllib

print(dir(urllib)) # Lists functions of imported Module
print(help(urllib.__builtins__))# provides helpful information of selected Module function
print()


# In this exercise, you will need to print an alphabetically sorted list of all functions in the re module, which contain the word find

import re

directory=dir(re)
for i in directory:
  if not i.find("find"):
    print(i)
_____________________________________________
https://www.learnpython.org/en/Numpy_Arrays

height=[1.87,1.87,1.82,1.91,1.90,1.85]
weight=[81.65,97.52,95.25,92.93,86.13,88.45]

import numpy as np

np_height=np.array(height) # np.array() converts list to Numpy Array
np_weight=np.array(weight)

print(height)
print(np_height)

print(weight)
print(np_weight)

bmi=np_weight/np_height**2

print(bmi)

print(bmi[bmi>25])
print()

# Exercise
weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Create a numpy array np_weight_kg from weight_kg
np_weight_kg=np.array(weight_kg)

# Create np_weight_lbs from np_weight_kg
np_weight_lbs=np_weight_kg*2.2


# Print out np_weight_lbs
for i in np_weight_lbs:
  print(str(i) + ' lbs')
  
  
  





