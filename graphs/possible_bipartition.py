# Can be used for BFS
from collections import deque
# This is DFS
def has_no_bad_cycle(cycle_counter_list, key, dislikes):
    # exits if the key is present in list => there is a cycle
    # AND
    # if the len of list(path) is odd => the cycle is NOT ok
    if len(cycle_counter_list) % 2 != 0 and cycle_counter_list[0] == key:
        return False
    
    # exits if the key is present in list => there is a cycle
    if key in cycle_counter_list:
        return True

    for value in dislikes[key]:
        if has_no_bad_cycle(cycle_counter_list + [key], value, dislikes) == False:
            return False

    return True

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    """
    - start with the "first" node
    - add the node and it's children to a 
    """
    
    for key in dislikes.keys():
        if has_no_bad_cycle(list(), key, dislikes) == False:
            return False
                # que.remove(item)

    return True

