# Can be used for BFS
from collections import deque


def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?

        Plan -> maybe make two lists and start by putting the first key in one and the values of that key in the other, then continue to separate it and check if 
    """
    if len(dislikes) == 0:
        return True

    groups = {key: 0 for key in dislikes.keys()}

    first_dog = list(dislikes.keys())[0]
    groups[first_dog] = 1
    queue = deque([first_dog])
    visited = set()

    while queue:
        curr_dog = queue.popleft()
        visited.add(curr_dog)

        if dislikes[curr_dog]:
            for disliked_dog in dislikes[curr_dog]:
                if groups[disliked_dog] == 0:
                    groups[disliked_dog] = groups[curr_dog] + 1
                    queue.append(disliked_dog)
                else:
                    if groups[disliked_dog] == groups[curr_dog]:
                        return False

        if len(queue) == 0:
            for dog in dislikes:
                if dog not in visited:
                    queue.append(dog)
                    break
    return True
