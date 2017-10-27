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
____________________________________________________________
https://www.learnpython.org/en/Multiple_Function_Arguments

def foo(first, second, third, *therest):
  print("First: " + first)
  print("Second: " + second)
  print("Third: " + third)
  print("And all the rest... ")
  for i in therest:
    print(i)
  

foo('Jeff', 'Jeffald', 'Jeffaldine', 'Cyril', 'Magoo', 'Maloy')
print()

def bar(first, second, third, **options):
  if options.get("action")=="sum":
    print("The sum is: %d" %(first+second+third))
    
  if options.get("number")=="first":
    return first

result=bar(1,2,3,action="sum", number = "first")
print("Result: " + str(result))

# edit the functions prototype and implementation
def foo(a, b, c, *d):
    return len(d)

def bar(a, b, c, **d):
    if d.get("magicnumber") !=7:
      return False
    if d.get("magicnumber")==7:
      return True


# test code
if foo(1,2,3,4) == 1:
    print("Good.")
if foo(1,2,3,4,5) == 2:
    print("Better.")
if bar(1,2,3,magicnumber = 6) == False:
    print("Great.")
if bar(1,2,3,magicnumber = 7) == True:
    print("Awesome!")
_________________________________________________
https://www.learnpython.org/en/Regular_Expressions
  
import re
pattern=re.compile(r"\[(on|off)\]")
print(re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]")) # Returns match
print(re.search(pattern, "Nada....:-")) # Returns None as no match found
print()


  # Exercise: make a regular expression that will match an email
def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(pattern, email):
            print("You failed to match %s" % (email))
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")
            print(email)
pattern = r"\S*.\S*.(\S*)" # ********** MY CODE ************
test_email(pattern)





















