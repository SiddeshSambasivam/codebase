t = int(input())

for i in range(t):
    n= int(input())
    if n<=4:
        print(0)
    else:
        add ,val, i =0,0,1
        while( n//(5**i) > 0):
            add+= n//(5**i)
            i+=1
        print(add)



