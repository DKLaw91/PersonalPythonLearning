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
