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

    # set up dictionaries
    for dog_key in dislikes:
        visited[dog_key] = False
        color[dog_key] = False

    # start checking for biparte
    for dog_key in dislikes:
        visited[dog_key] = True
        if not bipartition_helper(dislikes, dog_key, visited, color):
            return False
    return True

def bipartition_helper(dislikes, dog_key, visited, color):
    for dog in dislikes[dog_key]:
        # check if it's visited or not
        if not visited[dog]:
            visited[dog] = True
            # if it's not visited, change the color to opposite of the dog_key
            color[dog] = not color[dog_key]
            # recurse through that dog's enemies
            if not bipartition_helper(dislikes, dog, visited, color):
                return False
        elif color[dog] == color[dog_key]:
            return False
    return True
