
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

def daysInMonth(month,year):
    months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if(isLeapYear(year) and month == 2):
        months[2] = 29
    return months[month]

def nextDay(year, month, day):
    if day < daysInMonth(month,year):
        return year,month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1,1,1

def isLeapYear(year):
    isCenturyYear = year % 100 == 0 #Divisible by 100
    divisibleByFour = year % 4 == 0 #Divisible by 4, leap year in most cases
    divisibleBy400 = year % 400 == 0 
    leapYearException = isCenturyYear and not divisibleBy400
    
    if(divisibleByFour and not leapYearException):
        return True
    else: 
        return False
    
        
print(isLeapYear(2000))#True
print(isLeapYear(2004))#True
print(isLeapYear(2008))#True
print(isLeapYear(2001))#False
print(isLeapYear(2100))#False

daysBetweenDates(2000,1,1,2001,1,1)#365
daysBetweenDates(2000,1,1,2000,1,30)#29