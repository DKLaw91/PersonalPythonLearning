# > = Conveyor
# _ = Pit
# F = End of Conveyor
# # = Box

conveyorBelt=">>>>__>>__>_>>>F"
Boxes=[]
for i in range(0,len(conveyorBelt)):
    Boxes.append("")
count=0
while Boxes[conveyorBelt.index("F")] != "#":
    if conveyorBelt[count]=="_":
        conveyorBelt=conveyorBelt.replace("_", "#", 1)
        count-=1
    else:
        Boxes[count]="#"
    count+=1
    boxes=""
    for box in Boxes:
        boxes+=box
    print(boxes)
    print(conveyorBelt)
    print()
count=(count+(conveyorBelt.count("#"))+1)
print("Boxes reach end of Conveyor Belt at Timestep: " + str(count))
