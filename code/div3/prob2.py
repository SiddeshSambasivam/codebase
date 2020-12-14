import math

def merge(left, right):
    if len(left)==0:
        return right
    if len(right)==0:
        return left
    i,j=0,0
    result = list()
    while( (i<len(left)) and (j<len(right)) ):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i==len(left):
        result+=right[j:]
    if j==len(right):
        result+=left[i:]
    
    return result
def mergesort(a):
    if len(a)<=1:
        return a
    else:
        mid = len(a)//2
        left = a[:mid]
        right = a[mid:]
        return merge(mergesort(left),mergesort(right))

def function(a,b,k,n):
    a,b =  mergesort(a), mergesort(b)
    i,j = 0,n-1
    if b[j]<a[i]:
        return sum(a)
    for z in range(k):
        if b[j]>a[i]:
            a[i] = b[j]
            j-=1
        
        i+=1
    return sum(a)

t = int(input())
for t in range(t):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(function(a,b,k,n))