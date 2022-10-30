# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):

    if not dislikes or len(dislikes) == 1:
        return True

    dogs = list(dislikes.keys())

    dog = dogs[0]
    queue = [dog]
    the_haters = {}
    the_haters[dog] = 1

    for i in range(len(dogs)):
        if not queue and dogs[i] not in the_haters:
            queue.append(dogs[i])
            the_haters[dogs[i]] = 1
        while queue:
            current_dog = queue.pop(0)
            for other_dog in dislikes[current_dog]:
                if other_dog not in the_haters:
                    the_haters[other_dog] = 2 if the_haters[current_dog] == 1 else 1
                    queue.append(other_dog)
                if the_haters[other_dog] == the_haters[current_dog]:
                    return False

    return True