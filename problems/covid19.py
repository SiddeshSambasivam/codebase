from collections import defaultdict

def find_spread(n, dist):
    spread = []
    d1,d2 = [0]*n, [0]*n
    for i in range(0,n-1):
        d1[i]= abs(dist[i+1]-dist[i])
    for i in range(n-1, 0, -1):
        d2[i] = abs(dist[i]-dist[i-1])
    for i in range(n):
        inf =1
        for j in range(i, n-1):
            if d1[j]<=2 :
                inf +=1
            else:
                break
        for j in range(i,-1,-1):
            if d2[j]<=2 and d2[j]!=0:
                inf+=1
            else:
                break
        spread.append(inf)

    return [min(spread),max(spread)]

if __name__ == "__main__":

    T = int(input('T= '))
    for i in range(T):
        n = int(input('N= '))
        dist = list(map(int, input().rstrip().split()))
        result = find_spread(n, dist)
        print(*result, sep=" ")