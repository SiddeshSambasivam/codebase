"""
ID: plutocr1
LANG: PYTHON3
TASK: beads
"""


def countBeads(sleft: str, sright: str) -> int:

    sleft = ''.join(reversed(sleft))
    # print(sleft)
    lstack, lp = [], 1
    lstack.append(sleft[0])
    if len(sleft) > 1:
        while True:
            # print('Before Pop', lstack)
            ele = lstack.pop()

            if ele != sleft[lp]:
                if ele == 'w':
                    lstack += [sleft[lp]]*2
                    # print('After Pop(pop white)', lstack)
                    lp += 1
                elif sleft[lp] == 'w':
                    lstack += [ele]*2
                    lp += 1
                    # print('After Pop(string white)', lstack)
                else:
                    lstack += [ele]
                    # print('After Pop (Exit condn)', lstack)
                    break
            else:
                lstack += [ele]*2
                lp += 1
                # print('After Pop (add)', lstack)

    rstack, rp = [], 1
    rstack.append(sright[0])

    if len(sright) > 1:

        while True:
            ele = rstack.pop()
            if ele != sright[rp]:
                if ele == 'w':
                    rstack += [sright[rp]]*2
                    rp += 1
                elif sright[rp] == 'w':
                    rstack += [ele]*2
                    rp += 1
                else:
                    rstack += [ele]
                    break
            else:
                rstack += [ele]*2
                rp += 1

    print(f'\n{sright}', '\nright= ', len(rstack),
          f'\n{sleft}', '\nleft= ', len(lstack))
    print('Value= ', len(rstack)+len(lstack))
    print()

    return len(rstack)+len(lstack)


def solve(n: int, beads: str) -> int:
    _max = 0
    beads = beads * 2
    mid = len(beads)//2
    for i in range(n):
        val = countBeads(beads[:mid], beads[mid:])
        # print(
        #     f"Iteration {i}\nleft:  {beads[:mid]}\nright: {beads[mid:]}\n")

        if val >= _max:
            _max = val
        mid += 1
    print('maximum value = ', _max)
    fout = open('beads.out', 'w')
    fout.write(str(_max) + '\n')
    fout.close()


fin = open('beads.in', 'r')
n, beads = fin.read().splitlines()
n = int(n)
solve(n, beads)
