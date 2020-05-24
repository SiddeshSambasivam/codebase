a = []
for _ in range(int(input())):
    a.append(int(input()))
a.sort(reverse=True)
revenue = 0
for i in range(len(a)):
    revenue = max(revenue, a[i]*(i+1))
print(revenue)