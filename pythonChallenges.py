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


