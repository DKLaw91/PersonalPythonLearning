string="abcdeadsafewew"
print(string)
for letter in string:
    stringindex=string.index(letter)
    searchstring=string[stringindex+1:]
    repeatletlocation=""
    repeatletlocation=searchstring.find(letter)
    repeatedstring=""
    repeatedstring=searchstring[repeatletlocation]
    if repeatedstring == letter:
        print("The first recurring letter is: " + letter)
        print("First occurrance is at " + str((string.index(letter))+1))
        print("Second occurance is at " + str(repeatletlocation))
        break
