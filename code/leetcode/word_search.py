from typing import List
from itertools import product

def dfs(board:list, word:str, pos:tuple) -> bool:

    if len(word) < 1: return True

    x, y = pos
    branch_node_value = board[x][y]
    board[x][y] = "#"

    result = False

    directions = [(1,0), (0,1), (-1, 0), (0, -1)]

    for dx, dy in directions:
        
        if x+dx >=0 and x+dx < len(board) and y+dy >= 0 and y+dy < len(board[0]) :

            if (board[x+dx][y+dy] == word[0]):
                result = result or dfs(board, word[1:], (x+dx, y+dy))

        if result: return True

    board[x][y] = branch_node_value
    

    return False
    

def exist(board: List[List[str]], word: str) -> bool:

    if not word or len(board)*len(board[0]) < len(word) : return False

    m,n = len(board), len(board[0])

    for (x,y) in product(range(m), range(n)):

        if board[x][y] == word[0] and dfs(board, word[1:], (x,y)):
            return True

    return False

def run_tests():

    cases = [
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"), 
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"), 
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCD"), 
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABFDEEE"),
        ([["a"]], "a"),
        ([["a","b"],["c","d"]], "cdba"),
        ([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"),
        ]

    for i, (graph, test) in enumerate(cases):

        result = exist(graph, test)
        print(f"Case {i}, Query: {test}")
        for row in graph:
            print(row)
        print(f"Result: {result}")
        print()

run_tests()