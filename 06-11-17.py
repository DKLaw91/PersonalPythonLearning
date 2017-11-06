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



    









