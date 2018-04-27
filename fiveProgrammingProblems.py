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
numbers=[50,2,1,9] # 95021 desired output


def largestnum(numbers):
    stringnum=[]
    for number in numbers:
        stringnum.append(str(number))
    count=9
    returnnum=""
    while len(returnnum) != len(numbers)+1:
        for number in stringnum:
            if (count-int(number[0])) == 0:
                returnnum+=(number)
        if count != 0:
            count-=1
        else:
            count=9
    return int(returnnum)
        

print(largestnum(numbers))
    

# https://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour













