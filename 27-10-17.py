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










