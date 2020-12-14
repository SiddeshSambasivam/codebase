import math
import re
def function(n,k,s):
    correct = [0]*n
    keys = [m.start() for m in re.finditer('1',s)]
    pairs = {}
    for val in keys: 
        if val+3 <= n-1:
            pairs.update({val:val+3})
        else:
    print(pairs)
# t = input()
# for t in range(t):
#     n,k = list(map(int, input().split()))
#     s = input()
#     function(n,k,s)
function(9,2, '010001010')
