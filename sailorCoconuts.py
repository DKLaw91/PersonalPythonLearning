# https://www.reddit.com/r/dailyprogrammer/comments/43ouxy/20160201_challenge_252_easy_sailors_and_monkeys/

#Solution 1
n=5
coconuts=n
coconuts=(n**n)-(n-1)
print(coconuts)

#Solution 2
sailors=5

for n in range(1,10000):
    coconuts=n
    for num in range(1, sailors+1):
        coconuts=coconuts-1
        sailor=(coconuts/5)
        coconuts=coconuts-sailor
    if coconuts % 2 ==0:
        print(int(n))
        break
