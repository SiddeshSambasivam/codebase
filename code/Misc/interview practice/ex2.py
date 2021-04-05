for case in range(int(input())):

    n, k = list( map(int, input().split()) )

    timeline = list()
    for interval in range(n):
        start, end = list( map(int, input().split()) )
        for i in range(start, end+1):
            if i not in timeline:
                timeline.append(i)
        
    timeline = sorted(timeline)
    timeout, bots = k, 1
    for i in range(1, max(timeline)+1):
        if timeout == 0 and i+1 in timeline: # deploy in middle of harvest
            bots+=1
            timeout = k

        if timeout > 0: 
            timeout -= 1

    print("Case #{}: {}".format(case+1, bots))