

activities = {
    'CONTEST_WON':300,
    'TOP_CONTRIBUTOR':300,
    'BUG_FOUND':1,
    'CONTEST_HOSTED':50
}

for _ in range(int(input())):
    act, org = list(input().split())
    score, time = 0,0
    for _ in range(int(act)):
        inp  = list(input().split())
        if len(inp)==1:
            score+= activities[inp[0]]
        else:
            if inp[0] == 'CONTEST_WON' :
                if int(inp[1])>=20:
                    score+= activities[inp[0]]
                else:
                    score+= activities[inp[0]]+20-int(inp[1])
            else:
                score+= activities[inp[0]]*int(inp[1])
    if org == 'INDIAN':
        redeem = 200
    else:
        redeem = 400
    while( score >= redeem):
        time+= score//redeem
        score = score%redeem
    print(time)
    


