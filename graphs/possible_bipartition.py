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

    groups = {}
    
    for key in dislikes.keys():
        groups[key] = 0
    
    first_dog = list(dislikes.keys())[0]

    groups[first_dog] = 1
    queue = [first_dog]
    visited = []

    for dog in dislikes: 
        while queue:
            current_i = queue.pop(0)
            visited.append(current_i)

            if dislikes[current_i]:
                for frenemie in dislikes[current_i]:
                    if groups[frenemie] == 0:
                        groups[frenemie] = groups[current_i] + 1
                        queue.append(frenemie)
                    else:
                        if groups[frenemie] == groups[current_i]:
                            return False
            
        if dog not in visited:
            queue.append(dog)
    return True
