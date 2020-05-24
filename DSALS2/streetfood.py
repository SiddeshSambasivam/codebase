import math

for _ in range(int(input())):
    for _ in range(int(input())):
        profit = float('-inf')
        s,p,v = list(map(int, input().split()))
        if p%(s+1) == 0:
            split =p//(s+1)
        else:
            split = math.floor(p//(s+1))
        tmp = v*split
        profit = max(profit, tmp)
    print(profit)    
