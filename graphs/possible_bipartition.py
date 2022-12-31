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
    
    # Each dog will be sorted in either Group 1 or Group 2
    dog_groups = {dog:0 for dog in dislikes} # Dogs w/ value 0 are still unsorted

    # Choose a starting dog & place in Group 1
    first_dog = list(dislikes.keys())[0]
    dog_groups[first_dog] = 1

    # Initialize the queue; this is how we will keep track of neighbors
    # Keep track of which dogs haven't been sorted yet so they can be added to queue if queue is empty
    dogs_to_sort = [dog for dog in dislikes]
    queue = [first_dog]

    for dog in dog_groups:
        while queue:
            current_dog = queue.pop(0)
            dogs_to_sort.remove(current_dog)

            for dog in dislikes[current_dog]:
                if dog_groups[dog] == 0:
                    dog_groups[dog] = 2 if dog_groups[current_dog] == 1 else 1
                    if dog in dogs_to_sort:
                        queue.append(dog)
                elif dog_groups[dog] == dog_groups[current_dog]:
                    return False
        if dogs_to_sort:
            queue.append(dogs_to_sort[0])
        else:
            return True
