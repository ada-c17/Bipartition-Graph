# Can be used for BFS
from collections import deque
from tokenize import group 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    checked = {}
    queue = []
    for dog in dislikes.keys():
        if len(dislikes[dog]) > 0:
            if not dog in checked:
                checked[dog] = 0  
                queue.append(dog)     
            while queue:
                rival = queue.pop(0)
                for neighbour in dislikes[rival]:
                    if not neighbour in checked:
                        if checked[rival] == 0:
                            checked[neighbour] = 1
                        else:
                            checked[neighbour] = 0
                        queue.append(neighbour)
                    else:
                        if checked[rival] == checked[neighbour]:
                            return False
    return True






