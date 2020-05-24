t = int(input())

for _ in range(t):
    _ =int(input())
    speed = list(map(int, input().split()))
    cars, max_ = 1, speed[0]
    for j in range(1,n):
        if speed[j]<=max_:
            cars+=1
            max_ = speed[i]
    print(cars)
 