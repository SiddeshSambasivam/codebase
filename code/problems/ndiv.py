from collections import defaultdict
import math
import time

def sieve(n):
    primes= []
    is_prime = defaultdict(int)
    for i in range(2, int(math.sqrt(n))+1):
        if is_prime[i]==0:
            for j in range(i*i, n+1):
                if j%i ==0:
                    is_prime[j]=1
    i = 2
    while(i<n):
        if is_prime[i] == 0:
            primes.append(i)
        i+=1
    # print('Primes= ', *primes, sep=' ')
    return primes

a,b,n = list(map(int, input().split()))
primes = sieve(b)
result = 0

for num in range(a, b+1):
    k,i = num,0
    t = primes[i]
    total = 1
    while(t**2 <= num):
        count=0
        while(num%t == 0):
            count+=1
            num=int(num/t)
        total = total * (count+1)
        i+=1
        t = primes[i]
    if num !=1:
        total *=2
    if total == n :
        result+=1

print('Result = ', result)
    

        







