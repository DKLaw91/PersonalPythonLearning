days31=["January", "March", "May", "July", "August", "October", "December"]
days30=["April", "June", "September", "November"]
days28=["February"]

months={
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}

weekdays=["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

dayofdates={
    
}

inputyear=2018
inputmonth=4
inputday=28
inputtotal="(%d, %d, %d)" % (inputyear,inputmonth,inputday)

years=range(1,inputyear+1)

count=0

for year in years:
    for strmonth, intmonth in months.items():
        if strmonth in days31:
            days=range(1,32)
            for day in days:
                dayofdates[year,intmonth,day]=weekdays[count]
                count+=1
                if count >6:
                    count=0
        if strmonth in days30:
            days=range(1,31)
            for day in days:
                dayofdates[year, intmonth,day]=weekdays[count]
                count+=1
                if count >6:
                    count=0
        if strmonth in days28:
            year4=year%4
            year100=year%100
            year400=year%400
            if year4 == 0:
                if year100 == 0:
                    if year400 == 0:
                        days=range(1,30)
                        dayofdates[year, intmonth,day]=weekdays[count]
                        count+=1
                        if count >6:
                            count=0
                    else:
                        days=range(1,29)
                        dayofdates[year, intmonth,day]=weekdays[count]
                        count+=1
                        if count >6:
                            count=0
            else:
                days=range(1,29)
                dayofdates[year, intmonth,day]=weekdays[count]
                count+=1
                if count >6:
                    count=0



for day, key in dayofdates.items():
    if str(day) == inputtotal:
        print("%d/%d/%d is a %s" % (day[2], day[1], day[0], key))
        
        

    
    
