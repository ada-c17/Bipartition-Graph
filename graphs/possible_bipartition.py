# Can be used for BFS
from collections import deque 

def bipartition_helper(counter_list, key, dislikes):
    if len(counter_list) % 2 != 0 and counter_list[0] == key:
        return False
    if key in counter_list:
        return True
    for value in dislikes[key]:
        if bipartition_helper(counter_list + [key], value, dislikes) == False:
            return False
    return True

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    for key in dislikes.keys():
        if bipartition_helper(list(), key, dislikes) == False:
            return False
    return True

