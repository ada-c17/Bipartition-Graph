# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    # dislikes = { 
        # "Fido": [],
        # "Nala": ["Cooper", "Spot"],
        # "Cooper": ["Nala", "Bruno"],
        # "Spot": ["Nala"],
        # "Bruno": ["Cooper"]
        # }

    if not dislikes:
        return True

    dog_pen = {dog:0 for dog in dislikes}

    start_dog = list(dislikes.keys())[0]
    dog_pen[start_dog] = 1

    dog_list = [dog for dog in dislikes]
    queue = [start_dog]

    for dog in dog_pen:
        while queue: 
            current_dog = queue.pop(0)
            dog_list.remove(current_dog)

            for dog in dislikes[current_dog]:
                # if the disliked dog is not sorted in the dogpen
                if dog_pen[dog] == 0:
                    # make the value of the disliked dog in the group 
                    if dog_pen[current_dog] == 1:
                        dog_pen[dog] = 2
                    else:
                        dog_pen[dog] = 1
                    if dog in dog_list:
                        queue.append(dog)
                elif dog_pen[dog] == dog_pen[current_dog]:
                    return False
        if dog_list:
            queue.append(dog_list[0])
        else:
            return True

