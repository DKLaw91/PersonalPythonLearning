https://www.learnpython.org/en/Closures
________________________________________________
def printthrough(message):
  "This is the enclosing function"
  def printer():
    "The nested function"
    print(message)
  printer()

print(printthrough("Pass through"))
printer=printthrough("Pass through")
print(printer)

def print_msg(number):
  def printer():
    "Here we are using the nonlocal keyword"
    nonlocal number
    number=3
    print(number)
  printer()
  print(number)
print_msg(9)
print()

# Make a nested loop and a python closure to make functions to get multiple multiplication functions using closures. That is using closures, one could make functions to create multiply_with_5() or multiply_with_4() functions using closures.

# My code
def multiplier_of(num1):
  def multiplywith(num2):
    print(str(num2) + 'x' + str(num1) + '=')
    print(num2*num1)
  return multiplywith # Do not put (). Pass through without!
###################################

multiplywith5 = multiplier_of(5)
multiplywith5(9)

# EEEEYYYYYYYYYYYEEEEEEEEESSSSSSS!!!!!!! Finally!!!!
