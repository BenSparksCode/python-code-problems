# https://projecteuler.net/problem=19
# How many Sundays fell on the first of the month
# during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import time
start_time = time.time()

# SOLUTION CODE STARTS HERE

YEAR = 1901
MONTH = 1
DAY = 1
WEEKDAY = 2 # 1901/01/01 was a Tuesday
firstSundayCount = 0

def daysInMonth(monthNum: int, yr: int) -> int:
    # 30 day months
    if monthNum in [4, 6, 9, 11]:
        return 30
    # If Feb, handle leap years
    elif monthNum == 2:
        # 29 if leap year, otherwise 28
        if yr % 400 == 0 or (yr % 4 == 0 and yr % 100 != 0):
            return 29
        else:
            return 28
    # Otherwise its a 31 day month
    else:
        return 31

def loopAndCount(year: int, month: int, day: int, weekday: int):
    while year < 2001:
        # First check if day qualifies to be added to count
        if weekday == 7:
            if day == 1:
                global firstSundayCount
                firstSundayCount += 1
            weekday = 1
        else:
            weekday += 1 
        # Then increment all counters with rules
        if day == daysInMonth(month, year):
            day = 1
            if month < 12:
                month += 1
            else:
                month = 1
                year += 1
        else:
            day += 1

loopAndCount(YEAR, MONTH, DAY, WEEKDAY)
solution = firstSundayCount

# SOLUTION CODE ENDS HERE
print("SOLUTION:", solution)
print("--- %s seconds ---" % (time.time() - start_time))