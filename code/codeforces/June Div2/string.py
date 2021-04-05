
for _ in range(int(input())):
    s = str(input())
    count,i,n = 0,0, len(s)-1
    while(i<n):
        if s[i] != s[i+1]:
            count+=1
            i+=2
        else:
            i+=1
    # yyxyxxyx
    # 01234567
    print(count)