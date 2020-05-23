
for _ in range(int(input())):
    k, d0, d1 = list(map(int, input().split()))
    if (d0+d1)%5==0:
        print("NO")
        continue
    if k ==2:
        if (d0+d1)%3 ==0:
            print("YES")
        else:
            print("NO")
    else:
        grps = (k-3)//4
        summ = (d0 + d1) + ((d0+d1)%10) + (20 * grps)
        remain = (k-3)%4

        tmp,rem= (d0 + d1)%10, []
        for _ in range(3):
            rem.append((2*tmp)%10)
            tmp = (2*tmp)%10

        for i in range(remain):
            summ+=rem[i]
        if summ%3 == 0:
            print('YES')
        else:
            print("NO")
        

        