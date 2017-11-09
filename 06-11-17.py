def varandtypes():
  print("Jeff, to the print!")
  x="Jeff"
  if x =="Jeff":
    print("Jeff is x-cellent.")
  print("Hello, Jeff!")
  inp=input("How you doing?")
  if isinstance(inp, str):
    print("Brah.")
  myage=26
  print("Age: " + str(myage))
  myfloat=float(myage)
  print("Age as Float: " + str(myfloat))
  Jeff,Jeffald=26,22
  print("Jeff is " + str(Jeff))
  print("& Jeffald is " + str(Jeffald))
  print("Combined they are " + str(Jeff + Jeffald))
  
  
  # change this code
  mystring = "Hello"
  myfloat = float(10.0)
  myint = 20
  
  # testing code
  if mystring.lower() == "hello":
      print("String: %s" % mystring)
  if isinstance(myfloat, float) and myfloat == 10.0:
      print("Float: %f" % myfloat)
  if isinstance(myint, int) and myint == 20:
      print("Integer: %d" % myint)
#####################################
def lists():  
  mylist=[]
  mylist.append(1)
  mylist.append(2)
  mylist.append(3)
  othlist=[1,2,3]
  
  for i in mylist:
    print(i)
  for i in othlist:
    print(i)
  
  numbers = []
  strings = []
  names = ["John", "Eric", "Jessica"]
  
  # write your code here
  second_name = names[1]
  numbers.append(1)
  numbers.append(2)
  numbers.append(3)
  strings.append("Hello")
  strings.append("World")
  
  
  # this code should write out the filled arrays and the second name in the names list (Eric).
  print(numbers)
  print(strings)
  print("The second name on the names list is %s" % second_name)
#######################################
def basicoperators():
  number=1+2*3/4.0
  print(number) 
  remainder=11%3
  print(remainder)
  squared=7**2
  cubed=2**3
  print(squared)
  print(cubed)
  hello="Hello" + " " + "Jeff!"
  print(hello)
  lotsofhellos="Hello! " *3
  print(lotsofhellos)
  evens=[2,4,6,8]
  odds=[1,3,5,7,9]
  all=evens+odds
  print(all)
  print([1,2,3]*3)
  
  x = object()
  y = object()
  
  # TODO: change this code
  x_list = [x]*10
  y_list = [y]*10
  big_list = x_list+y_list
  
  print("x_list contains %d objects" % len(x_list))
  print("y_list contains %d objects" % len(y_list))
  print("big_list contains %d objects" % len(big_list))
  
  # testing code
  if x_list.count(x) == 10 and y_list.count(y) == 10:
      print("Almost there...")
  if big_list.count(x) == 10 and big_list.count(y) == 10:
      print("Great!")  
#########################################    
def stringformat():
  names=["Jeff", "Jeffald", "Jeffaldine"]
  ages=[26,22,21]
  x=0
  for i in ages:
    print("Hello, %s! You are %d years old." % (names[x], ages[x]))
     x+=1
  
  data = ("John", "Doe", 53.44)
  format_string = "Hello %s %s. Your current balance is $%.2f."

  print(format_string % (data[0], data[1], data[2]))
  
def basicstrop():
  astring="Jeff & Jeffald!"
  astring2="Jeff & Jeffald!"
  print("Single quotes are ' '")
  print(len(astring))
  print(len(astring2))
  if len(astring) == len(astring2):
    print("G'damn Jeff! It's Jeffald.")
  print(astring.index("f")) # Only returns first instance of letter
  print(astring.count("f")) # Returns number of all instances
  print(astring[0:4])
  print(astring[0:10:2]) # Returns 1st character through to 9th skipping every other
  print(astring[::-1]) # To reverse string
  print(astring.lower())
  print(astring.upper())
  if astring.startswith("Jeff"):
    print("Yeah Brah.")
  if not astring.endswith("Nah"):
    print("Nah Brah.")
  split=astring.split(" ")
  print(split)
  if "Jeff" in split:
    print("You found me!")
  if "Jeffaldine" not in split:
    print("Da fuq outta 'ere!")
#############################################
def conditions():
  name="Jeff"
  age=26
  print(name=="Jeff")
  print(name=="Jeffald")
  print(age==1)
  print(age==26)
  print(age<30)
  print()
  if name=="Jeff" and age==26:
    print("Looking aesthetic Jeff!")
  if name =="Jeff" or name=="Thor":
    print("You're New Doug!")
  print()
  names= ["Jeff", "Jeffald", "Jeffaldine"]
  if name in names:
    print("You're in!")
    print()
  if age ==26:
    print("26?! Noice!")
  else:
    print("Nah brah")
  print()
  names2=["Jeff", "Jeffald", "Jeffaldine"]
  print(names==names2)
  print(names is names2)
  print()
  print(not True)
  print(not False)
  print()
  
  
  # change this code
  number = 20
  second_number = 0
  first_array = [1,2,3]
  second_array = [1,2]
  
  if number > 15:
      print("1")
  
  if first_array:
      print("2")
  
  if len(second_array) == 2:
      print("3")
  
  if len(first_array) + len(second_array) == 5:
      print("4")
  
  if first_array and first_array[0] == 1:
      print("5")
  
  if not second_number:
      print("6")
  
conditions()
