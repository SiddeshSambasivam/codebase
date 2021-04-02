from collections import defaultdict
import logging

class Graph:

    def __init__(self, vertices:int) -> None:
        
        self.graph = defaultdict(list)
        self.V = vertices

        for i in range(0, self.V):
            self.graph[i] = []

    def add_edge(self, u:int, v:int ) -> None:
        ''' Adds a directed edge from Node:u to Node:v '''
        self.graph[u].append(v)

    def path_exists(self, start:int, end:int) -> bool:

        if start not in self.graph or end not in self.graph:
            logging.error("Start/End node is not in the graph")
            return False

        queue = list()
        visited = list()

        queue.append(start)

        # bfs
        while queue:

            node = queue.pop(0)

            if node == end:
                return True

            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    visited.append(neighbour)

        return True

    def __str__(self) -> str:
        print(self.graph)
        return ""

g = Graph(5)

g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(1,4)
g.add_edge(4,5)
g.add_edge(5,3)

print(g)

print(g.path_exists(3,5))
    
'''
---> 4 -> 5 -> 3
1 -> 2 -> 3
--------->

'''