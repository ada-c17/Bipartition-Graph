# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    def dfs(node, color, colored_nodes):
        colored_nodes[node] = color
        for neighbor in dislikes[node]:
            if neighbor in colored_nodes:
                if colored_nodes[neighbor] == color:
                    return False
            else:
                if not dfs(neighbor, 1 - color, colored_nodes):
                    return False
        return True
    
    colored_nodes = {}
    for node in dislikes:
        if node not in colored_nodes:
            if not dfs(node, 0, colored_nodes):
                return False
    return True

