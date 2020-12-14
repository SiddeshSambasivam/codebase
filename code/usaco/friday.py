"""
ID: plutocr1
LANG: PYTHON3
PROG: friday
"""

fout = open ('friday.out', 'w')

result = [0]*7

def isLeap(year:int) -> bool:
    if(year%100 == 0):
        if(year%400 == 0):
            return True
        else:
            return False
    elif(year%4 == 0):
        return True
    return False

def getdays(month, year):
    check = [1,3,5,7,8,10,12]
    if month == 2:
        if isLeap(year):
            days = 29
        else:
            days = 28
    else:
        if month in check:
            days = 31
        else:
            days = 30
    
    return days

def lastDay(month, year, start):
    
    remain = (getdays(month, year)%7)
    if start + remain >= len(result):
        last = start + remain - len(result)
    else:
        last = start + remain

    return last

def month(month, year, start):
    days = getdays(month, year)
    result[start-2]+=1

    return lastDay(month, year, start)

def solveYear(year:int, start:int):

    for mon in range(1,13):
        start = month(mon, year, start)

    return start

def solver(path:str) -> None:
    fin = open(path, 'r')
    n = int(fin.read().split()[0])
    start = 2
    for yr in range(1900, 1900+n):
        start = solveYear(yr, start)

# Day indices
# 0 -> sat
# ...
# 6 -> fri
# 2 -> mon

solver('friday.in')
output = " ".join(map(str,result)).strip()
fout.write (output + '\n')
fout.close()