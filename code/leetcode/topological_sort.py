from collections import defaultdict

class Graph:

    def __init__(self, vertices):

        self.nodes = defaultdict(list)
        self.V = vertices
    
    def add_edge(self, u, v):
        ''' 
        Adds a edge directed from u to v
        '''

        self.nodes[u].append(v)
    
    def check_dag(self) -> bool:

        # all nodes in the queue means that its prereq is satisfied

        stack = list()
        inorder = [0]*self.V
        visited = 0

        for k,v in self.nodes.items():

            for n in v:
                inorder[n] += 1            
            
        for i, val in enumerate(inorder):

            if val == 0:
                stack.append(i)
                
        while stack:

            idx = stack.pop()
            node = self.nodes[idx]
            
            for neighbour in node:

                inorder[neighbour] -= 1

                if inorder[neighbour] == 0:
                    stack.append(neighbour)                    

            visited += 1

        if visited == self.V:
            return True
        
        return False


def solve(prereq:list, numCourses:int) -> bool:

    graph = Graph(numCourses)
    for (u,v) in prereq:
        graph.add_edge(u,v)

    print(graph.nodes)

    print(graph.check_dag())
    return graph.check_dag()

def main():

    prereq = [[0,1], [1,2], [2,3], [2,4], [3,5], [4,5]]
    numCourses = 6

    solve(prereq, numCourses)

main()





        

