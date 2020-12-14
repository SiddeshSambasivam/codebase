
n = int(input())
a = sorted(list(map(int, input().split())))
if a[0] != 1:
    print(1)
else:
    f = 0
    for i in range(1,len(a)):
        if a[i]-a[i-1] != 1:
            f = 1
            print(i+1)
            break
    if f == 0:
        print(n)

    
    

