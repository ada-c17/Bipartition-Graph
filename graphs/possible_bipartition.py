# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N+E) (N is dogs, E is edges (dogs who got beef))
        Space Complexity: O(N) (nodes (dogs) reliant on amount of dogs)
    """
    # return true if dogs can be split into two groups
    # and no fighting will occur. otherwise return false.
    if not dislikes:
        return True

    # dict for dog groups. default is 0, other group is 1.
    kennel = { dog:0 for dog in dislikes }

    first_dog = list(dislikes.keys())[0]
    kennel[first_dog] = 1

    #BFS
    queue = [first_dog]
    visited = [first_dog]

    for dog in dislikes:
        while queue:
            current_dog = queue.pop(0)
            visited.append(current_dog)

            if dislikes[current_dog]:
                for angy_dog in dislikes[current_dog]:
                    if kennel[angy_dog] == 0:
                        kennel[angy_dog] = kennel[current_dog] + 1
                        queue.append(angy_dog)
                    else:
                        if kennel[current_dog] == kennel[angy_dog]:
                            return False
        if dog not in visited:
            queue.append(dog)

    return True                                

