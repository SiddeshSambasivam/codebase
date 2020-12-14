
t = int(input())

for i in range(t):
    sentence = str(input())
    if len(sentence)>10:
        print(sentence[0]+str(len(sentence)-2)+sentence[-1])
    else:
        print(sentence)
        