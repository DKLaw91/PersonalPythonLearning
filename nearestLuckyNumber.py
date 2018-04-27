numbers=[]

for number in range(1,1001):
    numbers.append(number)

def removeNum(numbers, num):
    remnum=num
    count=1
    newlist=[]
    for number in numbers:
        if count == remnum:
            count=1
        else:
            newlist.append(number)
            count+=1
    return newlist
    

numbers=removeNum(numbers, numbers[1])
count=1
while count != len(numbers):
    numbers=removeNum(numbers, numbers[count])
    count+=1
    
inputNum=228

def prevNum(inputNum, numbers):
    while inputNum not in numbers:
        inputNum-=1
    return inputNum
    
def nextNum(inputNum, numbers):
    while inputNum not in numbers:
        inputNum +=1
    return inputNum

prevLuckyNum=(prevNum(inputNum, numbers))
nextLuckyNum=(nextNum(inputNum, numbers))

if inputNum in numbers:
    print("%d is a lucky number" % inputNum)
else:
    print("%d > %d > %d" % (prevLuckyNum, inputNum, nextLuckyNum))
    
#https://www.reddit.com/r/dailyprogrammer/comments/6wjscp/2017828_challenge_329_easy_nearest_lucky_numbers/
