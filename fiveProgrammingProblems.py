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
# Largest Possible Number
numbers="17 32 91 7 46"

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
        onedigit.append(int(str(number)*2))


twodigits=[]
for number in list:
    if len(str(number)) == 2:
        twodigits.append(number)


combined=sortlist((onedigit+twodigits))



for number in combined:
    if number in onedigit:
        singledigit=int(str(number)[0])
        combined[combined.index(number)]=singledigit


largestnum=""

for num in combined:
    largestnum+=str(num)

print(largestnum)

# https://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour













