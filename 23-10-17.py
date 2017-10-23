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

