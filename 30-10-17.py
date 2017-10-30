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







