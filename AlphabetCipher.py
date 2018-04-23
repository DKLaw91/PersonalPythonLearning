Alphabet=["abcdefghijklmnopqrstuvwxyz"]
string=Alphabet[0]
#Populates Alphabet#
for Row in range(1,26):
    first=string[0]
    string=string[1:]
    string=string+first
    Alphabet.append(string)
#Populates Alphabet#
    
#Prints Alphabet#    
def printAlphabet(Alphabet):
    count=1
    for Row in Alphabet:
        print(str(count) + " " + Row)
        count+=1
#Prints Alphabet# 
    
codeDict={
    }
#Populates Dictionary with letters of alphabet matched to numbers#
def populateDict(dict):
    count=0
    for number in range(0,26):
        codeDict[Alphabet[0][count]]=number
        count+=1

def printDictionary(dict):
    for key, value in sorted(dict.items()):
        print(key + ":" + str(value))
#Populates Dictionary with letters of alphabet matched to numbers#

populateDict(codeDict)

keyword="cloak"
message="iamtheprettiestunicorn"
#Repeats keyword to match length of message#
keywordmatch=keyword
count=0
while len(keywordmatch) != len(message):
    keywordmatch=keywordmatch+keywordmatch[count]
    count+=1
print("Keyword: " + keyword)
print("Repeated Keyword: " + keywordmatch)
print("Message: " + message)
#Repeats keyword to match Length of message#

#Encodes message using codeDict#
count=0
encodedmessage=""
for letter in message:
    keywordletter=keywordmatch[count]
    encodedmessage=encodedmessage+Alphabet[codeDict[keywordletter]][codeDict[letter]]
    count+=1
print("Encoded Message: " + encodedmessage)
#Encodes message using codeDict#

#Decodes message using codeDict#
count=0
decodedmessage=""
for letter in encodedmessage:
    keywordletter=keywordmatch[count]
    indexofletter=Alphabet[codeDict[keywordletter]].index(encodedmessage[count])
    decodedmessage=decodedmessage+codeDict.keys()[(codeDict.values()).index(indexofletter)]
    count+=1
print("Decoded Message: " + decodedmessage)
#Decodes message using codeDict#



    

        





