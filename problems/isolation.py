

''' 
Correct Implementation

'''
t = int(input())

for i in range(t):
    n,q = map(int, input().split())
    string = input()
    mapper = {}
    for s in string:
        if s not in mapper:
            rep = string.count(s)
            mapper.update({s:rep})
                
    for i in range(q):
        length = 0
        query = int(input())
        
        for key, val in mapper.items():
            if val>query:
                length+= (val-query)
        print(length)


# def isolation(n, string, c):
#     ql, en= 0, []
#     for s in string:
#         if s not in en:
#             rep = string.count(s)
#             if rep >c:
#                 ql+= (rep-c)
#                 en.append(s)
#     return ql
    
# if __name__ == "__main__":
#     try:
#         T = int(input('T= '))
#         for i in range(T):
#             c = list()
#             n,q = list(map(int, input('N,Q= ').rstrip().split()))
#             s = str(input('String= '))
#             for i in range(q):
#                 c.append(int(input(f'Query {i+1}= ')))
#             for query in c:
#                 result = isolation(n, s, query)
#                 print(result)
#     except:
#         pass