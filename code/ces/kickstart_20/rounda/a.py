
for t in range(int(input())):
    n,b = list(map(int, input().split()))
    a = sorted(list(map(int, input().split())))
    count= 0
    for ele in a:
        if b >= ele:
            b-=ele
            count+=1

    print("Case #{}: {}".format(t+1, count))

        

