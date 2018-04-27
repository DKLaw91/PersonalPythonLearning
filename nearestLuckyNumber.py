numbers=[]

for number in range(1,1001):
    numbers.append(number)
    
remove2nd=filter(lambda i: i % 2 != 0, numbers)

def populatenumbers(numbers, filterlist):
    numbers=[]
    for number in filterlist:
        numbers.append(number)
    return(numbers)

def removeNum(numbers, num):
    remnum=num
    count=1
    newlist=[]
    for number in numbers:
        if count == remnum:
            count=1
            continue
        else:
            newlist.append(number)
            count+=1
    return newlist
    

numbers=removeNum(numbers, numbers[1])
count=1
while count != len(numbers):
    numbers=removeNum(numbers, numbers[count])
    count+=1
    
inputNum=997

def prevNum(inputNum, numbers):
    while inputNum not in numbers:
        inputNum-=1
    returnNum=inputNum
    return returnNum
    
def nextNum(inputNum, numbers):
    while inputNum not in numbers:
        inputNum +=1
    returnNum=inputNum
    return returnNum

prevLuckyNum=(prevNum(inputNum, numbers))
nextLuckyNum=(nextNum(inputNum, numbers))

if inputNum in numbers:
    print("%d is a lucky number" % inputNum)
else:
    print("%d > %d > %d" % (prevLuckyNum, inputNum, nextLuckyNum))
    
#https://www.reddit.com/r/dailyprogrammer/comments/6wjscp/2017828_challenge_329_easy_nearest_lucky_numbers/
