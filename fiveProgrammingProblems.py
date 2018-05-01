# 1. Sum of Numbers
usrinp=[12,85,78,88,64]

n=0
for number in usrinp:
    n+=number

print(n)

count=0
n=0
while count < len(usrinp):
    n+=usrinp[count]
    count+=1
print(n)

# 2. Merged Lists
list1=["a","b","c","d"]
list2=[1,2,3,4]
mergedlist=[]
count=0
for item in list1:
    mergedlist.append(list1[count])
    mergedlist.append(list2[count])
    count+=1

print(mergedlist)

# 3. Fibonacci Sequence
count=0
num=1
sequence=[count]
while count != 101:
    sequence.append(num)
    num+=sequence[count]
    count+=1
print(sequence)

# 4. Largest Possible Number
numbers="420 34 19 71 341"

########################################
def sortlist(numbers):
    returnlist=[]
    count=0
    while count != len(numbers):
        for number in numbers:
            returnlist.append(max(numbers))
            numbers.remove(max(numbers))
    return returnlist

list=[]
for number in numbers.split(" "):
    list.append(int(number))


onedigit=[]
for number in list:
    if len(str(number)) == 1:
        onedigit.append(int(str(number)*3))


twodigits=[]
for number in list:
    if len(str(number)) == 2:
        twodigits.append(int(str(number)+str(number)[1]))


threedigits=[]
for number in list:
    if len(str(number)) == 3:
        threedigits.append(number)



combined=sortlist((onedigit+twodigits+threedigits))



for number in combined:
    if number in onedigit:
        singledigit=int(str(number)[0])
        combined[combined.index(number)]=singledigit
    elif number in twodigits:
        doubledigits=int(str(number)[0:2])
        combined[combined.index(number)]=doubledigits


largestnum=""

for num in combined:
    largestnum+=str(num)

print(largestnum)

# 5. Output Possibilities
import random

target=100

possibilities=[]

answer=0

while answer != target:
    count=1
    possibility=""
    for n in range(1,10):
        while n <= 8:
            nextnum=n+1
            for f in range(1,4):
                f=random.randint(1,3)
                if possibility=="":
                    possibility=str(n)
                elif f == 3:
                    possibility=("".join(possibility+str(nextnum)))
                    break
                elif f ==2:
                    possibility+=("-"+str(nextnum))
                    break
                elif f ==1:
                    possibility+=("+"+str(nextnum))
                    break
            if "9" in possibility:
                if eval(possibility) == 100:
                    if possibility not in possibilities:
                        possibilities.append(possibility)
                        if len(possibilities)==11:
                            answer=100
                break
            else:
                break
        continue

possibilities=sorted(possibilities)
for p in possibilities:
    print(p)

# https://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour

