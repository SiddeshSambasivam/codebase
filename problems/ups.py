

def merge(left, right):
    if len(left)==0:
        return right
    if len(right)==0:
        return left
    result,i,j = [],0,0

    while( (i<len(left)) and (j<len(right)) ):
        if left[i] <= right[j] :
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

t  = int(input())

for i in range(t):

    n = int(input())
    a = list(map(int, input().split()))
    a = mergesort(a)
    for i in range(n):
        if i%2 != 0:
            a[i], a[i+1]=a[i+1], a[i]
    
    print(*a, sep=' ')
