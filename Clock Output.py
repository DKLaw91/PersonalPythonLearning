hours = {
  "00":"twelve",
  "01":"one",
  "02":"two",
  "03":"three",
  "04":"four",
  "05":"five",
  "06":"six",
  "07":"seven",
  "08":"eight",
  "09":"nine",
  "10":"ten",
  "11":"eleven",
  "12":"twelve",
  "13":"one",
  "14":"two",
  "15":"three",
  "16":"four",
  "17":"five",
  "18":"six",
  "19":"seven",
  "20":"eight",
  "21":"nine",
  "22":"ten",
  "23":"eleven",
}

minutes = {
  "00":"",
  "01":"one",
  "02":"two",
  "03":"three",
  "04":"four",
  "05":"five",
  "06":"six",
  "07":"seven",
  "08":"eight",
  "09":"nine",
  "10":"ten",
  "11":"eleven",
  "12":"twelve",
  "13":"thirteen",
  "14":"fourteen",
  "15":"fifteen"
}





usrinp=(str(input("Current Time? (HH:MM)")))
print(usrinp[0:2])
hrinp=(hours[usrinp[0:2]])
mininp=(minutes[usrinp[3:]])
def ampm():
  if int(usrinp[0:2]) >= 12:
    return "pm"
  else:
    return "am"


if mininp == "":
  print("It's %s %s" % (hrinp, ampm()))
else:
  print("It's %s oh %s %s" % (hrinp, mininp, ampm()))
  
  
  
  
  
  
  
  
  
  














