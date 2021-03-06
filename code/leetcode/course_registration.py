from collections import defaultdict
from typing import List

class Graph:

    def __init__(self, vertices:int):

        self.nodes = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        '''
        Adds a edge directed from node-u to node-v
        '''

        self.nodes[u].append(v)

    def schedule(self)  -> List[int]:
        '''
        Topological sorting of the graph and check if its DAG
        '''

        stack = list()
        course_order = list()

        inorder = [0] * self.V

        # need the inorder of all the nodes
        for k, v in self.nodes.items():
            for node in v:
                inorder[node] += 1
        
        for i, order in enumerate(inorder):

            if order == 0:
                stack.append(i)
            
        while stack:

            node = stack.pop()
            for neighbour in self.nodes[node]:

                inorder[neighbour] -= 1
                if inorder[neighbour] == 0:
                    stack.append(neighbour)
            
            course_order.append(node)
        
        if len(course_order) != self.V:
            return []

        return course_order


def solve(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    
    graph = Graph(numCourses)

    # a,b : b -> a
    for (v,u) in prerequisites:
        graph.add_edge(u,v)
    
    order = graph.schedule() 
    print(f"Course Order: {order}")

    return order

solve(2, [[1,0]])