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
        return False
    first_item = list(dislikes.keys())[1]
    stack = [first_item]
    result = True
    group_1 = []
    group_2 = []
    
    for pet in dislikes:
        group_1.append(dislikes[pet])
        group_2.append(pet)
        if pet in group_1 and pet in group_2:
            result = False
        if pet not in group_1 and pet not in group_2:
            result = True
    if len (group_1) and len(group_2) == 0:
        return False
    
    return result


