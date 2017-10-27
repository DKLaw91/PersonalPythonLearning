https://www.learnpython.org/en/Generators
________________________________________________
import random

def lottery():
  for i in range(5):
    yield random.randint(1,40)
    
  for i in range(2):
    yield random.randint(1,2)
    
for random_number in lottery():
  print("And the next number is... " + str(random_number))
print()

# fill in this function

def fib():
    a, b = 1, 1
    print(a)
    print(b)
    while True:
      c=a+b
      yield c
      a=b
      b=c

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
______________________________________________________________
https://www.learnpython.org/en/List_Comprehensions
  
sentence="Good old Jeff, the best of the best."
words=sentence.split()
word_lengths=[]
for word in words:
  if word != "the":
    word_lengths.append(len(word))
print(words)
print(word_lengths)
print()

# Alternative to above called List Comprehension
word_lengths=[len(word) for word in words if word != "the"]
print(words)
print(word_lengths)

# Exercise: Using a list comprehension, create a new list called "newlist" out of the list "numbers", which contains only the positive numbers from the list, as integers.
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(number) for number in numbers if number >0]
print(newlist)










