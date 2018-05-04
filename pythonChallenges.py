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
