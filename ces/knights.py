n = int(input())
for i in range(1,n+1):
    a = i**2 * ((i**2 -1)) // 2
    b = 4* (i-1) * (i-2)
    print(a-b)