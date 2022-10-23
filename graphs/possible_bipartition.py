# Can be used for BFS
from collections import deque

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N + E) where N is the number of nodes, E is the number of edges
        Space Complexity: O(N) where N is the number of nodes (or dogs)
    """
    if not dislikes: 
        return True

    groups = {}
    # {'Fido': 0, 'Nala': 0, 'Cooper': 0, 'Spot': 0, 'Bruno': 0}
    for key in dislikes.keys():
        groups[key] = 0
    
    first_dog = list(dislikes.keys())[0]

    groups[first_dog] = 1
    queue = [first_dog]
    visited = []

    for dog in dislikes: 
        while queue:
            current_dog = queue.pop(0)
            visited.append(current_dog)

            if dislikes[current_dog]:
                for frenemie in dislikes[current_dog]:
                    if groups[frenemie] == 0:
                        groups[frenemie] = groups[current_dog] + 1
                        queue.append(frenemie)
                    else:
                        if groups[frenemie] == groups[current_dog]:
                            return False
            
        if dog not in visited:
            queue.append(dog)
    return True
