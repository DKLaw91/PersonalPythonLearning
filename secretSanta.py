# https://www.reddit.com/r/dailyprogrammer/comments/3yiy2d/20151228_challenge_247_easy_secret_santa/

import random

usrinp="""Sean
Winnie
Brian Amy
Samir
Joe Bethany
Bruno Anna Matthew Lucas
Gabriel Martha Philip
Andre
Danielle
Leo Cinthia
Paula
Mary Jane
Anderson
Priscilla
Regis Julianna Arthur
Mark Marina
Alex Andrea"""

lines=usrinp.splitlines()
names=usrinp.split()
line={}
santa=[]

count=1
for l in lines:
    line[count]=l.split(" ")
    count+=1

def removename(list, name):
    newlist=[i for i in list if i != name]
    return newlist

def checkline(lines, name1, name2):
    result=False
    for line in lines:
        if name1 in line and name2 in line:
            result=True
    return result



for name in names:
    namelist=removename(names, name)
    for n in namelist:
        if checkline(lines, name, n):
            namelist.remove(n)
    santalines=[]
    for line in santa:
        santalines.append(line.split())
    count=0
    namestoremove=[]
    if len(santalines) > 0:
        while count != len(santalines):
            namestoremove.append(santalines[count][2])
            for name in namestoremove:
                if name in namelist:
                    namelist.remove(name)
            count+=1
    randintmax=len(namelist)-1
    if randintmax == 0:
        output=namelist[0]
    else:
        output=namelist[random.randint(0,randintmax)]
    santa.append(("%s --> %s" % (name, output)))

santalines=[]
for line in santa:
    santalines.append(line.split())
    print(line)

    
