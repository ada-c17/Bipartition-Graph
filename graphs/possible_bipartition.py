# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N + E) where n represents the amount of nodes and E represents the amount of edges in total from each of the nodes
        Space Complexity: O(N) where n represents the amount of nodes, i.e. dogs in this problem
    """
    """
    EXAMPLE 1:
    dislikes = { 
        "Fido": [],
        "Nala": ["Cooper", "Spot"],
        "Cooper": ["Nala", "Bruno"],
        "Spot": ["Nala"],
        "Bruno": ["Cooper"]
        }

    TRUE 

    EXAMPLE 2:
    dislikes = {
        "Fido": [],
        "Nala": ["Cooper", "Spot"],
        "Coooper": ["Nala", "Spot"],
        "Spot": ["Nala", "Cooper"]
    }

    FALSE 
    """

    if not dislikes: 
        return True 

    groups = {}
    for dog in dislikes.keys():
        groups[dog] = 0 

    first_dog = list(dislikes.keys())[0]
    groups[first_dog] = 1
    queue = [first_dog]
    visited = []

    for dog in dislikes: 
        while queue:
            current_dog = queue.pop(0)
            visited.append(current_dog)

            if dislikes[current_dog]:
                for neighbor in dislikes[current_dog]:
                    if groups[neighbor] == 0:
                        groups[neighbor] = groups[current_dog] - 1 # this works regardless of if you subtract or add 1?
                        queue.append(neighbor)
                    else:
                        if groups[current_dog] == groups[neighbor]:
                            return False 
            
        if dog not in visited:
            queue.append(dog)

    return True 

