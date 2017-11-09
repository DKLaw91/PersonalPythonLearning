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
##################################################
def loops():
  primes=[2,3,5,7]
  for i in primes:
    print(i)
  print()
  
  names=["Thor", "Hulk", "Loki", "Heimdall"]
  for i in names:
    print(i)
  print()
  
  for x in range(1,6):
    print(x)
  print()
  
  for x in range(1,10,2):
    print(x)
  print()
  
  count=1
  while count<11:
    print(count)
    count +=1
  print()
  
  count=1
  while True:
    print(count)
    count+=1
    if count >=11:
      break
  print()
  
  for x in range(10):
    if x%2==0:
      continue
    print(x)
  print()
  
  count=1
  while(count<11):
    print(count)
    count+=1
  else:
    print("Count value exceeded %d" %(count-1))
  print()
  
  for i in range(1,10):
    if i%5==0:
      break
    print(i)
  else:
    print("This is not printed because for loop is terminated because of break but not due to fail in condition.")
  print()
    
  numbers = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527]
  
  for i in numbers:
    if i%2==0:
      print(i)
    if i==237:
      break
###################################################################
def functions():
  def names():
    names=["Thor", "Loki", "Odin", "Hela"]
    for i in names:
      print(i)
    print()
  names()
  def slapped(slapper, slappee):
    print(slapper + " pwopah slapt " + slappee + ".")
    print()
  slapped("Valkyrie", "Loki")
  def sum(a,b):
    return a+b
    print()
  print(sum(12,15))
  
  # Modify this function to return a list of strings as defined above
  def list_benefits():
      return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]
      
  
  # Modify this function to concatenate to each benefit - " is a benefit of functions!"
  def build_sentence(benefit):
      print(benefit + " is a benefit of functions")
  
  def name_the_benefits_of_functions():
      list_of_benefits = list_benefits()
      for benefit in list_of_benefits:
          print(build_sentence(benefit))
  
  name_the_benefits_of_functions()
###############################






