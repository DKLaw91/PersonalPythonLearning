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
