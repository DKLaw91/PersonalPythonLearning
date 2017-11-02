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
    
