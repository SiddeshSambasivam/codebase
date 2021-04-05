
T = int(input())
for i in range(T):
    
    n, x = list(map(int, input().split()))
    array = list(map(int, input().split()))
    
    '''
    1. Iterate through the queue and calculate the number of turns 
    required to withdraw the rquired amount for a given person and store 
    it in a dictionary, with position in queue as key with the number 
    of turns as key.
    
    2. Sort the dict by its values and the position with smallest 
    value leaves the queue first.
    
    '''

    turns2pos = dict()
    for pos, amt in enumerate(array):
        if amt % x != 0:
            turns2pos[pos]  = (amt // x) + 1
        else:
            turns2pos[pos]  = (amt // x) 
        
    turns = [ (pos+1, turn) for pos, turn in sorted(turns2pos.items(), key=lambda item: item[1])]
    
    # Equal turns, three consecutive equal turns
    results = list()
    for i in range(n):
        results.append(turns[i][0])    
    
    print("Case #{}:".format(i),*results, sep=' ')    
    
    