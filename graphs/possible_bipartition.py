# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """

    def is_bipartite(dislikes, item, visited, color):
        for name in dislikes[item]:
            if visited[name] == False:
                visited[name] = True
                color[name] = not color[item]
                if not is_bipartite(dislikes, name, visited, color):
                    return False
            elif color[name] == color[item]:
                return False
        return True

    if not dislikes:
        return True
    
    visited = {}
    color = {}

    for each_key in dislikes:
        for item in dislikes:
            visited[item] =  False
            color[item] = False
        
        first_key = each_key
        visited[first_key] = True
        color[first_key] = False
        if not is_bipartite(dislikes, first_key, visited, color):
            return False
    return True

