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
        
    dogs_to_check = list(dislikes.keys())
    if len(dislikes) == 1:
            return True
    first_dog = dogs_to_check[0]
    queue = [first_dog]
    dog_groups = {}
    dog_groups[first_dog] = 1
    
    for i in range(1, len(dogs_to_check)):
        if not queue and dogs_to_check[i] not in dog_groups:
            queue.append(dogs_to_check[i])
            dog_groups[dogs_to_check[i]] = 1
        while queue:
            current_dog = queue.pop(0)
            for other_dog in dislikes[current_dog]:
                if other_dog not in dog_groups:
                    dog_groups[other_dog] = 2 if dog_groups[current_dog] == 1 else 1
                    queue.append(other_dog)
                if dog_groups[other_dog] == dog_groups[current_dog]:
                    return False
            
    return True

