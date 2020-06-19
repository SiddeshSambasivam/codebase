
for _ in range(int(input())):
    x,y = list(map(int, input().split()))
    m = max(x,y)
    ans = ( m*(m-1)+1 ) + ( (-1)**m ) * (x-y)
    print(ans)

            

