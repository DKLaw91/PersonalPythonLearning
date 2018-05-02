# https://www.reddit.com/r/dailyprogrammer/comments/5961a5/20161024_challenge_289_easy_its_super_effective/

usrinp="Fire->Grass"
split=usrinp.split("->")
type1=split[0].lower()
type2=split[1].lower()


normal, fire, water, electric, grass, ice, fighting, poison, ground, flying, psychic, bug, rock, ghost, dragon, dark, steel, fairy = {},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}

strtypes=["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"]

for t in strtypes:
    for s in strtypes:
        eval(t)[s]=1

def changekey(dict, noeffect,half,double):
    for i in dict:
        if i in noeffect:
            dict[i]=0
        elif i in half:
            dict[i]=0.5
        elif i in double:
            dict[i]=2
        else:
            dict[i]=1
    return dict
            

normal=changekey(normal,["ghost"],["rock","steel"],[])

fire=changekey(fire,[],["fire","water","rock","dragon"],["grass","ice","bug","steel"])


for k,v in eval(type1).items():
    if k == type2:
        print(usrinp)
        print("%dx Attack" % v)
