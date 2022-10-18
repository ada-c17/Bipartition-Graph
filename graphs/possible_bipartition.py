# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    # if input dict is empty or has 1 element -> return True
    if not dislikes or len(dislikes) == 1:
        return True

    # there are 2 groups: 15 and 20
    # dict to keep dogs and their groups like:
    # {
    #    Fido: 15,
    #    Nala: 20,
    #    Bruno: 15,
    #    ...
    # }
    groups = {}

    list_of_dogs = list(dislikes.keys())
    first_dog = list_of_dogs[0]
    queue = [first_dog]

    groups[first_dog] = 15


    for i in range(len(list_of_dogs)):
        if not queue and list_of_dogs[i] not in groups:
            queue.append(list_of_dogs[i])
            groups[list_of_dogs[i]] = 15

        while queue:
            current_dog = queue.pop(0)
            # loop through the list of dislikes dogs of current dog
            for dislike_dog in dislikes[current_dog]:
                if dislike_dog not in groups:
                    if groups[current_dog] == 15:
                        groups[dislike_dog] = 20
                    else:
                        groups[dislike_dog] = 15
                    # add dislike_dog to queue only if its not in groups
                    queue.append(dislike_dog)
                if groups[dislike_dog] == groups[current_dog]:
                    return False

    return True

