
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)

### Define a daysBetweenDates procedure that would produce the 
### correct results given a correct nextDay procedure

def daysBetweenDates(year1,month1,day1,year2,month2,day2):
    currentDate = year1,month1,day1 
    endDate = year2,month2,day2
    days = 0
    while(currentDate < endDate): 
        currentDate = nextDay(*currentDate)
        days += 1
    return days


def nextDay(year, month, day):
    if day < 30:
        return year,month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1,1,1


daysBetweenDates(2000,1,1,2000,1,3)