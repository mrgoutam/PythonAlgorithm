"""
------------------------INFO----------------------------------------------
Breath First Traversal(or Search) for a graph is similar to Breath First
Traversal of a tree. The only catch here is, unlike trees, graphs may
contain cycles, so we may come to the same node again. To avoid processing
a node more than once, we use a boolean visited or explored array. For
simplicity, it is assumed that all vertices are reachable from the starting
vertex.

Pseudo-code:
BFS(graph G, start vertex s):
// all nodes initially unexplored
mark s as explored
let Q = queue data structure, initialized with s
while Q is non-empty:
    remove the first node of Q, call it v
    for each edge(v, w):  // for w in graph[v]
        if w unexplored:
            mark w as explored
            add w to Q (at the end)
--------------------------------------------------------------------------
"""
# to create a list graph, please see 01_graph_list.py
G = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

def breath_first_search(graph, start):
    explored, queue = set(), [start]
    explored.add(start)
    while queue:
        v = queue.pop(0)
        for item in graph[v]:
            if item not in explored:
                explored.add(item)
                queue.append(item)
    return explored

if __name__=='__main__':
    print('Breath First Search: ')
    print(breath_first_search(G,  'A'))

'''
------------------------OUTPUT BOX----------------------------------------
Breath First Search: 
{'F', 'B', 'C', 'D', 'E', 'A'}
--------------------------------------------------------------------------
'''