# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """

    if len(dislikes) == 0:
        return True

    graph = {}
    color = {}
    
    for dislike in dislikes:
        graph[dislike] = dislikes[dislike]
    
    for node in graph:
        if node not in color:
            color[node] = 0
            queue = deque()
            queue.append(node)
            while queue:
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[curr]
                        queue.append(neighbor)
                    elif color[neighbor] == color[curr]:
                        return False
    return True


