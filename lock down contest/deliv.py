from  math import gcd

n,r= list(map(int, input().split()))
dist = list(map(int, input().split()))

dist.sort()

result = abs(dist[0]-r)
for i in range(1, n):
    result = gcd(result, abs(dist[i]-r))
print(result)
