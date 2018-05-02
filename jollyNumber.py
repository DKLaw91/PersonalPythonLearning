# https://www.reddit.com/r/dailyprogrammer/comments/65vgkh/20170417_challenge_311_easy_jolly_jumper/

usrinp="4 19 22 24 25"
split=usrinp.split(" ")
numbers=[]
firstint=int(split[0])
for n in split[1:]:
    numbers.append(int(n))
diff=[firstint]
count=1
n=numbers[count]
while len(diff) != len(numbers):
    for num in numbers:
        addnum=abs(n-num)
        diff.append(addnum)
        if count != len(numbers)-1:
            count+=1
            n=numbers[count]
        else:
            break
diff=sorted(diff)
count=1
compnum=diff[count]
answer=[]
for num in diff:
    if abs(num-compnum) == 1:
        answer.append(True)
    else:
        answer.append(False)
    if count != len(diff)-1:
        count+=1
        compnum=diff[count]
    else:
        break
        

if False in answer:
    print("%s = NOT JOLLY" % usrinp)
else: 
    print("%s = JOLLY" % usrinp)
