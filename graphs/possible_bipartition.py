# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    if not dislikes:
            return True

    visited = {}
    color = {}

    for dog_name in dislikes:
        visited[dog_name] = False
        color[dog_name] = False
            
    for dog_name in dislikes:
        visited[dog_name] = True
        if not helper_func(dislikes, dog_name, visited,color):
            return False
    return True

def helper_func(dislikes, dog_name, visited, color):
    for dog in dislikes[dog_name]:
        if not visited[dog]:
            visited[dog] = True
            color[dog] = not color[dog_name]
            if not helper_func(dislikes, dog, visited, color):
                return False
        elif color[dog] == color[dog_name]:
            return False
    return True
