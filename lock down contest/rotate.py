
for _ in range(int(input())):
    n, r =  list(map(int, input().split()))
    result = [None for i in range(n)]
    array =  list(map(int, input().split()))
    for i, ele in enumerate(array):
        idx = r-n+i
        result[idx]=ele
    print(*result, sep=' ')