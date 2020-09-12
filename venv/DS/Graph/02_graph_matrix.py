class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = [[0]*vertex for i in range(vertex)]
        print('Empty Matrix:\n', self.graph)

    def add_edge(self, u, v):
        self.graph[u-1][v-1] = 1
        self.graph[v-1][u-1] = 1

    def print_graph(self):
        print('\nAdjacent Matrix:')
        for i in self.graph:
            for j in i:
                print(j, end=" ")
            print(" ")

g = Graph(5)
g.add_edge(1, 4)
g.add_edge(4, 2)
g.add_edge(4, 5)
g.add_edge(2, 5)
g.add_edge(5, 3)
g.print_graph()

'''
------------------------OUTPUT BOX----------------------------------------
Empty Matrix:
 [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

Adjacent Matrix:
0 0 0 1 0  
0 0 0 1 1  
0 0 0 0 1  
1 1 0 0 1  
0 1 1 1 0  
--------------------------------------------------------------------------
'''