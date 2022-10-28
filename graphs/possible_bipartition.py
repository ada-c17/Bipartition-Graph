# Can be used for BFS
from collections import deque 

# dislikes = {
#              "Fido": [],
#              "Nala": ["Cooper", "Spot"],
#              "Cooper": ["Nala", "Spot"],
#              "Spot": ["Nala", "Cooper"]
#              }

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    

    dog_groups = {}

    # if len(dislikes) == 0:
    #     return True

    for i in dislikes:
        if i not in dog_groups:
            stack = [i]
            dog_groups[i] = 0
            while stack:
                i = stack.pop()
                for dog in dislikes[i]:
                    if dog not in dog_groups:
                        stack.append(dog)
                        dog_groups[dog] = 1 - dog_groups[i]
                    elif dog_groups[dog] == dog_groups[i]:
                        return False
    return True

