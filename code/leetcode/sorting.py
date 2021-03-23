
def merge(left: list, right: list) -> list:
    '''Merges any two sorted arrays'''

    result = list()

    while left and right:

        if left[0] >= right[0]:
            ele = right.pop(0) # add right[0] to the result
            result.append(ele)
        else:
            ele = left.pop(0) # add left[0] to the result
            result.append(ele)            

    if left:
        result += left
    elif right:
        result += right

    return result

def merge_sort(array:list) -> list:
    '''
    Sorts the input array in the ascending order and returns it
    '''

    if len(array) <= 1:
        return array

    # Pointer which points to the middle of the given input array
    mid = len(array)//2

    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    result = merge(left, right)

    return result


def bubble_sort(array:list) -> list:
    '''
    Sorts the array comparing all combinations of elements in the array
    '''
    
    for i in range(0, len(array)):
        for j in range(i, len(array)):

            if array[i] >= array[j]:
                array[i], array[j] = array[j], array[i]

    return array

def partition(array: list, left:int, right:int) -> list:

    pivot = array[left]
    i, j = left, right

    while(i<j):

        while(i<len(array) and array[i] <= pivot):
            i += 1

        while(j>=0 and array[j] >= pivot):
            j -= 1

        if(i<j):
            array[i], array[j] = array[j], array[i]

    array[left], array[j] = array[j], array[left]

    return [array, j]
    

def quick_sort(array:list, left:int, right:int) -> list:

    if len(array) <= 1:
        return array

    if left < right:

        array, idx = partition(array, left, right)
        array = quick_sort(array, left, idx-1)
        array = quick_sort(array, idx+1, right)

    return array

test_case = [9,5,1,8,2,7,3,4]

print(merge_sort([9,5,1,8,2,7,3,4]))
print(bubble_sort([9,5,1,8,2,7,3,4]))
print(quick_sort([9,5,1,8,2,7,3,4], 0, len(test_case)-1))
