
n = int(input())
if (n*(n+1))%4 != 0:
    print("NO")
else:
    if n%2 != 0:
        msum, tsum= n*(n+1)//4 , n
        b = [k for k in range(1,n)]
    
        a = [n]
        i,j = n-2, 0
        
        while(tsum<=msum):
            tsum += b[i]
            print(b[i])
            a.append(b.pop(i))
            if tsum >= msum:
                break
            tsum += b[j]
            print(b[j])
            a.append(b.pop(j))
            print(tsum)
            i-=1 
            j+=1
        print(sorted(a))
        print(sorted(b))

    


