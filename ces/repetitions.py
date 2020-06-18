
i, s = 0, str(input())
max_len, tmp=  0, ''
for ele in s:
    if tmp == ele:
        count+=1
    else:
        count= 1
    tmp = ele
    if count >= max_len:
        max_len = count
        
print(max_len)

