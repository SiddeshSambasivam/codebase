
t = int(input())

for _ in range(t):
    g = int(input())
    for _ in range(g):
        head = 0
        tail = 0
        i,n,q = list(map(int, input().split()))
        #i=1 ->head
        #i=2 ->Tail
        if n%2 == 0:
            print(n//2)
        else:
            if i == 1:
                if q ==1 :
                    print(n//2)
                elif q==2:
                    print(n//2 +1)
            elif i == 2:
                if q ==1 :
                    print(n//2+1)
                elif q==2:
                    print(n//2)

