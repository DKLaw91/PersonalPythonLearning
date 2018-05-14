# https://old.reddit.com/r/dailyprogrammer/comments/83uvey/20180312_challenge_354_easy_integer_complexity_1/

inpnum=834
options=[]

for num1 in range(inpnum):
    for num2 in reversed(range(inpnum)):
        if num1*num2 == inpnum:
            options.append(num1+num2)

if options == []:
    print("%d => %d" % (inpnum,inpnum+1))
else:
    print("%d => %d" % (inpnum, options[int(len(options)/2)]))
