
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)

### Define a daysBetweenDates procedure that would produce the 
### correct results given a correct nextDay procedure

def daysBetweenDates(year1,month1,day1,year2,month2,day2):
    days = 0
    #force an incorrect result to be true, then flip it to false to trigger an assertion error
    assert  not dateIsBefore(year2, month2, day2, year1, month1, day1) 
    while dateIsBefore(year1,month1,day1,year2,month2,day2): 
        year1,month1,day1 = nextDay(year1,month1,day1)
        days += 1
    print(days)
    return days

def dateIsBefore(year1,month1,day1,year2,month2,day2):
    result = False
    if(year1 < year2):
        result = True
    if(year1 == year2):
        if month1 < month2:
            result = True
        if month1 == month2:
            if day1 < day2:
                    result = True
    return result

def daysInMonth(month):
    months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    return months[month]

def nextDay(year, month, day):
    if day < daysInMonth(month):
        return year,month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1,1,1


daysBetweenDates(2000,1,1,2001,1,1)