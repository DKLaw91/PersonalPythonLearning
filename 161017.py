int1=7
print(int1)

float1=7.0
print(float1)

float1=float(7.00)
print(float1)

print('##########')

string1='hello'
print(string1)

string1="hello"
print(string1)

string2="don't worry about apostrophes"
print(string2)

string2='don\'t worry about apostrophes'
print(string2)

print('##########')

print('''I can print
on multiple lines
just look here.''')

print('##########')

one=1
two=2
three=one + two
print(three)

hello='hello'
world='world'
helloworld=hello + ' ' + world
print(helloworld)

hello, world = 'hello', 'world'
print(hello)
print(world)

print('##########')

mystring=input('string = ')
myfloat=float(input('float = '))
myint=int(input('integer = '))

if mystring == 'hello':
  print('String: ' + mystring)
if myfloat == 10.00:
  print('Float: ' + str(myfloat))
if myint == 20:
  print('Integer: ' + str(myint))

print('##########')

mylist=[]
mylist.append(input('Name? '))
mylist.append(input('Age? '))
mylist.append(input('Gender? '))

for i in mylist:
  print(i)

print('#############')

numbers=[]
strings=[]
names=['John', 'Eric', 'Jeff']

numbers.append(1)
numbers.append(2)
numbers.append(3)
print(numbers)

strings.append('hello')
strings.append('world')
print(strings)

second_name=names[1]
print('The second name on the list is: ' + second_name)

print('#########'
______________________________________________________________________________________
https://www.learnpython.org/en/Basic_Operators
number1=int(input('First Number? '))
number2=int(input('Second Number? '))
number3=int(input('Third Number? '))
number=(number1+number2*number3)
print(number)

print('########')

remainder= number1 % number2
print(remainder)

print('########')

squared= number2**2
print(squared)

cubed=(number2**3)
print(cubed)

print('########')

helloworld= 'Jeff' + ' is hench on the bench'
print(helloworld)

lotsofjeffs='Jeff ' * 10
print(lotsofjeffs)

even=[2,4,6,8]
odd=[1,3,5,7,9]
allnumbers=even + odd
print(allnumbers)

jeff=(['jeff', 'hench']*3)
print(jeff)

print('########')

x='x'
y='y'

x_list=[x,x,x,x,x,x,x,x,x,x]
y_list=[y,y,y,y,y,y,y,y,y,y]
big_list=x_list + y_list
print('x_list contains: ' + str(len(x_list)))
print('y_list contains: ' + str(len(y_list)))
print(big_list)

if x_list.count(x) == 10 and y_list.count(y) == 10:
  print('Almost there...')
  
print(big_list.count(x))
print(big_list.count(y))
  
if big_list.count(x) == 10 and big_list.count(y) == 10:
  print('Great!')
      
______________________________________________________________________________________
name='Jeff'
print('Hello, %s!' % name)
age=23
print('%s is %s years old.' % (name, age))

print('%.2f' % age)
print('%X' % age)

print('###############')

data=('John', 'Doe', 53.44)
format_string='Hello '

print(data[0])
print(data[1])
print(data[2])

print(format_string + '%s %s. Your current balance is £%.2f.' % (data[0], data[1], data[2]))
____________________________________________________________________________________________
https://www.learnpython.org/en/Basic_String_Operations
astring='Hello World!'
astring2='Hello World!'

print("single quotes are ' '")
print(len(astring))

print(astring.index('o'))

print(astring.count('l'))

print(astring[6:11])

print(astring[::-1])

print(astring.startswith('Hello'))
print(astring.endswith('dasda'))

afewwords=astring.split(' ')
print(afewwords)

print('##############')
      
------------------------------------------------------------------------------------------
s="Strands are welcome!"
print("Length of s = %d" % len(s))

print("The first occurrence of the letter a = %d" % s.index('a'))

print("a occurs %d times" % s.count('a'))

print("The first five characters are '%s'" % s[:5])
print("The next five characters are '%s'" % s[5:10])
print("The thirteenth character is '%s'" % s[12])
print("The characters with odd index are '%s'" % s[1::2])
print("The last five characters are '%s'" % s[-5:])

print("String in uppercase: %s" % s.upper())

print("String in lowercase: %s" % s.lower())

if s.startswith("Str"):
  print("String starts with 'Str'. Good!")

if s.endswith("ome!"):
  print("String ends with 'ome!'. Good!")

print("Splite the words of the string: %s" % s.split(' '))
