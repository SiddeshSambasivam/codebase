"""
ID: plutocr1
LANG: PYTHON3
TASK: gift1
"""

def getInputs(path) -> dict:
    fin = open (path, 'r')
    inputs = fin.read().splitlines()
    n = int(inputs[0])
    persons = inputs[1:n+1]
    iterator = iter(inputs[n+1:])
    master = dict()
    for i in range(len(persons)):
        person = next(iterator)
        amt, pep  = map(int, next(iterator).split())
        value = 0
        if amt != 0 and pep != 0:
            value = amt//pep
        giving_to = []
        
        for _ in range(pep):
            b = next(iterator)
            giving_to.append(b)

        master[person] = [
            [amt, pep, value], giving_to
        ]

    return master, persons

def solve(inputs:dict, group:list) -> None:
    results = {}

    for key, _ in inputs.items():
        results[key] = 0
        # gives -> add
        # pay -> subtract
    
    for k, v in inputs.items():

        # amount, number of people, idv_pay, balance
        accounts, people = v
        amt, num, pay = accounts
        results[k] -= num*pay
        
        for p in people:
            results[p] += pay

    fout = open ('gift1.out', 'w')
    for person in group:
        fout.write (person + ' ' + str(results[person]) + '\n')
    fout.close()
    # print(results)
    

inputs, group = getInputs('gift1.in')
solve(inputs, group)
