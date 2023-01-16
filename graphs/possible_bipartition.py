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

    dog_group = {dog: 0 for dog in dislikes}
    dog_list = [dog for dog in dislikes]
    first_dog = list(dislikes.keys())[0]
    q = [first_dog]

    for dog in dog_group:
        while q:
            current = q.pop(0)
            dog_list.remove(current)

            for dog in dislikes[current]:
                if dog_group[dog] == 0:
                    if dog in dog_list:
                        q.append(dog)
                        
                    if dog_group[current] == 1:
                        dog_group[dog] = 2
                    else:
                        dog_group[dog] = 1
                    
                
                elif dog_group[dog] == dog_group[current]:
                    return False
        
        if dog_list:
            q.append(dog_list[0])
        else:
            return True


