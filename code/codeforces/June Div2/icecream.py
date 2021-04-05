
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if a[0]==5:
        #  5 10 5 10 15 5
        cash, f = 0, 0
        for i in range(n):
            if a[i] == 5:
                cash+=5
                continue
            if abs(cash-a[i]) == 5:
                cash = 5
            elif abs(cash-a[i]) == 0:
                cash-=5
            else:
                f=1
                print("NO")
                break
        if f == 0:
            print("YES")
    else:
        print("NO")