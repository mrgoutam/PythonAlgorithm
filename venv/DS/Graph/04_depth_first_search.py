"""
------------------------INFO----------------------------------------------
The DFS function simply calls itself recursively for every unvisited child of
its argument. We can emulate that behaviour precisely using a stack of iterators.
Instead of recursively calling with a node, we'll push an iterator to the node's
children onto the iterator stack. When the iterator at the top of the stack
terminates, we'll pop it off the stack.

Pseudo-code:
    all nodes initially unexplored
    mark s as explored
    for every edge (s, v):
        if v unexplored:
            DFS(G, v)
--------------------------------------------------------------------------
"""

G = {
    "A": ["B", "C", "D"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "D"],
    "E": ["B", "F"],
    "F": ["C", "E", "G"],
    "G": ["F"],
}

def depth_first_search(graph, start: str):
    explored, stack = set(start), [start]
    while stack:
        v = stack.pop()
        # one difference from BFS is to pop last element here instead of first one
        for w in graph[v]:
            if w not in explored:
                explored.add(w)
                stack.append(w)
    return explored

if __name__ == "__main__":
    print('Depth First Search: ')
    print(depth_first_search(G, "A"))

"""
------------------------OUTPUT BOX----------------------------------------
Depth First Search: 
{'C', 'F', 'D', 'A', 'G', 'E', 'B'}
--------------------------------------------------------------------------
"""