# https://www.reddit.com/r/dailyprogrammer/comments/52enht/20160912_challenge_283_easy_anagram_detector/

inp="Reddit?Eat Dirt"

inp=inp.split("?")
first=inp[0].replace(" ", "")
second=inp[1].replace(" ", "")
print(first, second, "\n")

firstlist=[]
secondlist=[]

for letter in first:
    firstlist.append(letter.lower())

for letter in second:
    secondlist.append(letter.lower())

firstlist=sorted(firstlist)
secondlist=sorted(secondlist)

def comparelists(list1, list2):
    if len(list1) != len(list2):
        return("%s is NOT an anagram of %s" % (inp[1], inp[0]))
    else:
        combined=[l for l,o in zip(firstlist,secondlist) if l == o]
        if combined == list1 and combined == list2:
            return("%s is an anagram of %s" % (inp[1], inp[0]))
        else:
            return("%s is NOT an anagram of %s" % (inp[1], inp[0]))

answer=comparelists(firstlist, secondlist)
print(answer)
