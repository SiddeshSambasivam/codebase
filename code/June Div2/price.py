
for _ in range(int(input())):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    tmp = 0
    for ele in a:
        if ele > k:
            tmp += ele - k
    print(tmp)

