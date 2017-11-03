https://www.learnpython.org/en/Decorators
______________________________________________-

def repeater(oldfunc): # Decorator to repeat function twice
  def newfunc(*args, **kwds): 
    oldfunc(*args, **kwds)
    oldfunc(*args, **kwds)
  return newfunc

@repeater # Used to call Decorator on Function
def multiply(num1, num2):
  print(num1*num2)

multiply(12,86)
print()

def Dblout(oldfunc):
  def newfunc(*args, **kwds):
    return 2*oldfunc(*args, **kwds) # Modify the return value
  return newfunc

def Dblin(oldfunc):
  def newfunc(arg): # Will only work if oldfunc has one argument
    return oldfunc(arg*2) # Modify the argument passed
  return newfunc

def check(oldfunc):
  def newfunc(arg):
    if arg<0: raise ValueError("Negative Amount") # Returns error message if argument below 0
    oldfunc(arg)
  return newfunc

@check
def num(num):
  print(num)

num(15)
num(-15)
print()

def multiplier(multiplier):
  def multiplygen(oldfunc):
    def newfunc(*args, **kwds):
      return multiplier*oldfunc(*args, **kwds)
    return newfunc
  return multiplygen

@multiplier(5) # Defines multiplier
def num(num):
  return num # Will not work with print() as return string not integer

print(num(15))
print()

# Make a decorator factory which returns a decorator that decorates functions with one argument. The factory should take one argument, a type, and then returns a decorator that makes function should check if the input is the correct type. If it is wrong, it should print("Bad Type". (In reality, it should) raise an error, but error raising isn't in this tutorial.) Look at the tutorial code and expected output to see what it is if you are confused (I know I would be.) Using isinstance(object, type_of_object) or type(object) might help.

def type_check(correct_type):
    # My Code
    def newfunc(oldfunc):
      def checker(num):
        if isinstance(num, correct_type):
          return oldfunc(num)
        else:
          print("Error: Bad Type")
      return checker
    return newfunc

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])
