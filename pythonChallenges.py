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
