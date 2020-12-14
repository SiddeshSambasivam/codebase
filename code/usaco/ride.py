"""
ID: plutocr1
LANG: PYTHON3
PROG: ride
"""
fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')

comet, group = fin.read().split()

def getValue(string:str)->int:
    value = 1
    for char in string:
        value *= (ord(char)-64)
    return value

def decide(comet:str, group:str) -> None:
    
    c,g = getValue(comet), getValue(group)
    if (c%47 == g%47):
        fout.write ("GO" + '\n')
    else:
        fout.write('STAY' + '\n')

decide(comet, group)

