
n = int(input())
if n==1:
    print(1)
elif n < 4 :
    print("NO SOLUTION")
else:
    a = [i for i in range(1,n+1) if i%2==0] + [i for i in range(1,n+1) if i%2!=0]
    print(*a)