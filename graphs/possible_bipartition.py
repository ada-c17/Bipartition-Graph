# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """

    if not dislikes or len(dislikes) == 1:
        return True
        
    dogs = list(dislikes.keys())
    
    first_dog = dogs[0]
    queue = [first_dog]
    dog_fight = {}
    dog_fight[first_dog] = 1
    
    for i in range(len(dogs)):
        if not queue and dogs[i] not in dog_fight:
            queue.append(dogs[i])
            dog_fight[dogs[i]] = 1
        while queue:
            current_dog = queue.pop(0)
            for other_dog in dislikes[current_dog]:
                if other_dog not in dog_fight:
                    dog_fight[other_dog] = 2 if dog_fight[current_dog] == 1 else 1
                    queue.append(other_dog)
                if dog_fight[other_dog] == dog_fight[current_dog]:
                    return False
            
    return True