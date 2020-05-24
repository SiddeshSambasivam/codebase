import math

t = int(input())
for i in range(t):
    n = int(input())
    j,s = len(str(n))-1,0
    while(n>0):
        r = n%10
        n = n//10
        s+=r*math.pow(10,j)
        j-=1
    print(int(s) )
