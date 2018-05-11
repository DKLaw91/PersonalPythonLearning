def dartscore(sect,darts,targ):
    def retsco(score,darts):
        for n in score:
            return n * darts
    points=[[i for i in sect]for i in range(darts)]
    poss=[]
    for d1 in points[0]:
        for d2 in points[1]:
            for d3 in points[2]:
                if d1+d2+d3==targ:
                    darts=sorted([d1,d2,d3])
                    if ("%d-%d-%d" % (darts[0],darts[1],darts[2])) not in poss:
                        poss.append("%d-%d-%d" % (darts[0],darts[1],darts[2]))
    if poss==[]:
        print("No solution!")
    else:
        for p in poss:
            print(p)


dartscore([3,6,8,11,15,18,22],3,32)
