import math

def subarr(a,n):
    if sum(a) == 0:
        return [1, n]
    

    # for i in range()
    
    

#know the problem
def function(n):
    a = [0]*(n+1)
    for i in range(n):
        l,r = subarr(a,n)
        # print(l,r)
        if (r - l +1 )%2 == 0:
            a[int((l+r)/2)]=i
        else:
            a[int((l+r-1)/2)+1]=i
    print(*a[1:], sep=' ')

# t = input()
# for t in range(t):
#     n = int(input())
#     function(n)
function(2)