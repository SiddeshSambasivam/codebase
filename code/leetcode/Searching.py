from sorting import merge_sort

def binary_search(array:list, query:int) -> int:

    start, end = 0, len(array)-1

    while(start<=end):

        mid = (start + end)//2

        if array[mid] == query:
            return mid

        if array[mid] > query:

            end = mid-1

        else:

            start = mid + 1
        
    return -1


    return 0 

def main(array:list, query:int) -> int:

    print("Unsorted array: ", array)
    sorted_array = merge_sort(array)
    print("Sorted array: ", sorted_array)

    idx = binary_search(sorted_array, query)

    print(f'Element {query} found at index {idx}')

main([91, 4123,43,234,4423,22,3,42,5,2,15], 234)
