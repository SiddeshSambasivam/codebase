
t = int(input())

for i in range(t):
    s = str(input())
    mid = len(s)//2
    flag = 0
    if len(s)%2!=0:
        s = s[:mid]+s[mid+1:]

    for l in s:
        if s[:mid].count(l) != s[mid:].count(l):
            flag = 1
            break

    if flag == 1:
        print('NO')
    else:
        print('YES')