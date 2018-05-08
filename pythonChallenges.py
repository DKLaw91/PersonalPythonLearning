# https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt

1. 
answer=[]

for n in range(2000,3201):
    if n % 7 == 0 and n % 5 != 0:
        answer.append(str(n))
    
print(",".join(answer))

2. 
usrinp=8
count=usrinp-1
answer=usrinp
for n in range(usrinp, 1, -1):
    answer=answer*count
    count-=1

print(answer)

####################################
    
def factorial(n):
    return n * factorial(n-1)
    
print(fact(8))

3.
mydict={}
usrinp=12
for n in range(1, usrinp+1):
    mydict[n]=n*n
print(mydict)

4.
usrinp=("34,67,55,33,12,98")

numbers=usrinp.split(",")
tup=tuple(numbers)
print(numbers)
print(tup)

5.
class OutputString(object):
    def __init__(self):
        self.self=self
    
    def getString(self):
        self.getstring=input("")
    
    def printString(self):
        print("Yo! Jeff!")
    
string=OutputString()
string.printString()

6.
import math

C,H,Q=50,30,0
D=("100,150,180")
numbers=[]
output=[]

for n in D.split(","):
    numbers.append(int(n))

for n in numbers:
    Q=int(math.sqrt((2*C*n)/H))
    output.append(str(Q))

print(",".join(output))

7.
X=3
Y=5

array=[]

for r in range(0,X):
    array.append([0 for i in range(0,Y)])
    for c in range(0,Y):
        array[r][c]=r*c
print(array)

8.
usrinp="without,hello,bag,world"

words=sorted(usrinp.split(","))
print(",".join(words))

9.
usrinp="Hello world, I am Jeff!"

print(usrinp.upper())

10.
usrinp="hello world and practice makes perfect and hello world again"

words=sorted(set(usrinp.split(" ")))
print(words)

11.
usrinp="0100,0011,1010,1001"
numbers=[b for b in usrinp.split(",")]
for b in numbers:
    n=(int(str(b),2))
    if n%5==0:
        print(b)

12.
numbers=[]
for n in range(1000,3001):
    number=""
    for d in str(n):
        if int(d)%2==0:
            number+=d
    if len(number)==4:
        numbers.append(number)
print(",".join(numbers))

13.
usrinp="Hello World! 123"
split=usrinp.split(" ")
words=[i.strip("123456789") for i in split if i.strip("123456789") != ""]
num=[i for i in split if i not in words]
letters=0
for w in words:
    for l in w:
        if l.isalpha():
            letters +=1
digits=0
for n in num:
    digits+=len(n)
print("LETTERS: %d" % letters)
print("DIGITS: %d" % digits)

14.
usrinp="Hello world!"
usrinp=[i for i in usrinp if i.isalpha()]
upper=[i for i in usrinp if i.istitle()]
lower=[i for i in usrinp if i not in upper]
print("UPPER CASE: %d \nLOWER CASE: %d" % (len(upper), len(lower)))

15.
usrinp=9
def answer(n):
    s=str(n)
    s2=int(s*2)
    s3=int(s*3)
    s4=int(s*4)
    return int(s)+s2+s3+s4

print(answer(usrinp))

16.
usrinp=1,2,3,4,5,6,7,8,9
squareodd=[i*i for i in usrinp if i % 2 != 0]
print(squareodd)

17.
account=0

usrinp="D 300\nD 300\nW 200\nD 100"

t=usrinp.splitlines()
for l in t:
    if l.split(" ")[0] == "D":
        account+=int(l.split(" ")[1])
    elif l.split(" ")[0] == "W":
        account-=int(l.split(" ")[1])
print(account)

18.
usrinp="ABd1234@1,a F1#,2w3E*,2We3345"

attempts=usrinp.split(",")

def checkletter(p):
    for l in p:
        if l.isalpha():
            return True
    return False

def checkcap(p):
    for l in p:
        if l.istitle():
            return True
    return False

def checknum(p):
    for l in p:
        if l.isalnum():
            return True
    return False

def checkchar(p):
    for l in p:
        if l in ["$","#","@"]:
            return True
    return False


for p in attempts:
    if len(p)>=6 and len(p)<=12:
        if checkletter(p):
            if checkcap(p):
                if checknum(p):
                    if checkchar(p):
                        print(p)

19.
from operator import itemgetter
newdict={
    0:("Tom",19,80),
    1:("John",20,90),
    2:("Jony",17,93),
    3:("Jony",17,91),
    4:("Json",21,85)
}

sortlist=sorted(newdict.values(),key=itemgetter(0,1,2))
print(sortlist)
    
20.
class numgen(object):
    def __init__(self):
        self.self=self
    def returnlist(self,num):
        self.num=num
        return [n for n in range(1,num) if n % 7 ==0]

num1=numgen()
print(num1.returnlist(100))

21.
usrinp="UP 5, DOWN 3, LEFT 3, RIGHT 2"

direction=[w for w in usrinp.split(" ") if w.isalpha()]
nums=[int(n[0]) for n in usrinp.split(" ") if n not in direction]

position={"x":0,"y":0}

count=0
for m in direction:
    if m == "UP":
        position["x"]+=int(nums[count])
    elif m == "DOWN":
        position["x"]-=int(nums[count])
    elif m == "RIGHT":
        position["y"]+=int(nums[count])
    elif m == "LEFT":
        position["y"]-=int(nums[count])
    count+=1

fromstart=(abs(position["x"]-0)+abs(position["y"]-0))

print("Starting Position: 0,0")
print("Current Position: %d,%d" % (position["x"],position["y"]))
print("User is %d moves from starting position." % fromstart)

22.
usrinp="Hello, my name is Jeff. Jeff is my name, so it is, so it is!"

def wordcount(usrinp):
    words=["".join(l for l in w if l.isalnum()) for w in usrinp.split(" ")]
    remdup=sorted(set(words))
    for w in remdup:
        print("%s:%d" % (w,words.count(w)))

wordcount(usrinp)

23.
def square(num):
    return num**2

print(square(5))

24.
def square(num):
    """Return the Square Number of a given value"""
    return num**2
    
print(square.__doc__)
print(abs.__doc__)

25.
class Person(object):
    name="person's"
    age="years of age"
    def __init__(self,name,gender,age):
        self.name=name
        if gender=="m":
            self.gender="he"
        elif gender=="f":
            self.gender="she"
        self.age=age

Jeff=Person("Jeff","m",18)
print("This %s name is %s and %s is %d %s" % (Person.name, Jeff.name, Jeff.gender, Jeff.age, Person.age))
Jeffaldine=Person("Jeffaldine","f",24)
print("This %s name is %s and %s is %d %s" % (Person.name, Jeffaldine.name, Jeffaldine.gender, Jeffaldine.age, Person.age))

26.
def sumofnum(num1,num2):
    return num1+num2

print(sumofnum(12,45))

27.
def inttostr(int):
    print(str(int))

inttostr(45)

28.
def calculatestr(str):
    num1=str.split(" ")[0]
    num2=str.split(" ")[1]
    print(int(num1)+int(num2))

calculatestr("45 78")

29.
def joinstr(str1,str2):
    print(str1 + " " + str2)

joinstr("Hello","Jeff")

30.
def printlongest(str1,str2):
    if len(str1)>len(str2):
        print(str1)
    elif len(str1)<len(str2):
        print(str2)
    else:
        print(str1/n)
        print(str2)

printlongest("Jeffald","Jeff")
printlongest("Jeff","Jeff")

31.
def evenodd(num):
    if num % 2 == 0:
        print("%d is an even number." % num)
    else:
        print("%d is an odd number." % num)

evenodd(45)
evenodd(68)

32.
def printdict(num):
    dict={}
    for n in range(1,num+1):
        dict[n]=n**2
    print(dict)

printdict(10)

33.
def printdict(num):
    dict={}
    for n in range(1,num+1):
        dict[n]=n**2
    print(dict)

printdict(20)

34.
def printdict(num):
    dict={}
    for n in range(1,num+1):
        dict[n]=n**2
    for v in dict.values():
        print(v)
printdict(20)

35.
def printdict(num):
    dict={}
    for n in range(1,num+1):
        dict[n]=n**2
    for k in dict:
        print(k)
printdict(20)

36.
def printlist(num):
    list=[]
    for n in range(1,num+1):
        list.append(n**2)
    print(list)
printlist(20)

37.
def printlist(num):
    list=[]
    for n in range(1,num+1):
        list.append(n**2)
    print(list[0:5])
printlist(20)

38.
def printlist(num):
    list=[]
    for n in range(1,num+1):
        list.append(n**2)
    print(list[-5:])
printlist(20)

39.
def printlist(num):
    list=[]
    for n in range(1,num+1):
        list.append(n**2)
    print(list[5:])
printlist(20)

40.
def printtuple(num):
    list=[]
    for n in range(1,num+1):
        list.append(n**2)
    list=tuple(list)
    print(list)
printtuple(20)

41.
def printtuple(tup):
    print(tup[0:int(len(tup)/2)])
    print(tup[int(len(tup)/2):])

printtuple((1,2,3,4,5,6,7,8,9,10))

42.
def printtuple(tup):
    list=[i for i in tup if i % 2 ==0]
    print(tuple(list))

printtuple((1,2,3,4,5,6,7,8,9,10))

43.
tup=1,2,3,4,5,6,7,8,9,10
list=[i for i in tup if i % 2 ==0]
tup2=tuple(list)
print(tup2)

44.
inp="YES"

if inp.lower() == "yes":
    print("Yes")
else:
    print("No")

45.
inp=[1,2,3,4,5,6,7,8,9,10]

filtered=filter(lambda n:n%2==0, inp)
print(list(filtered))

46.
inp=[1,2,3,4,5,6,7,8,9,10]

squares=map(lambda n:n**2, inp)
print(list(squares))

47.
inp=[1,2,3,4,5,6,7,8,9,10]

output=map(lambda n:n**2, (filter(lambda n:n%2==0, inp)))
print(list(output))

48.
Question:
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

Hints:

Use filter() to filter elements of a list.
Use lambda to define anonymous functions.
