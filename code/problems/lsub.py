s, n= str(input()), 5
d = [input() for i in range(n)]

for w in s:
    count = 0
    for l in w:
        if l not in s:
            continue

        count+=1


