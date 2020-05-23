# Merge Sort

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

if __name__ =='__main__':
    a= list(map(int, input('Enter numbers: ').split()))
    print('\nBefore Sorting: ', *a, sep=' ')
    a = mergesort(a)
    print('After Sorting: ', *a, sep=' ')