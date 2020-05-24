
n,k = list(map(int, input().split()))
a =  list(map(int, input().split()))
res = 0
if a[k-1]<=0:
    print(0)
else:
    
    res+=len(a[:k])
    res+=a[k:].count(a[k-1])
    print(res)
