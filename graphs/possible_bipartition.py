# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    if len(dislikes) == 0:
        return True

# solution with que
    # group1 = []
    # group2 = []
    # puppies = list(dislikes.keys())
    # first_dog = puppies[0]
    # q = [first_dog]
    # group1.append(first_dog)
    # while q:
    #     current = q.pop(0)
    #     puppies.remove(current)
    #     if current not in group1 and current not in group2:
    #         group1.append(current)
    #     for dog in dislikes[current]:
    #         if dog not in group1 and dog not in group2:
    #             q.append(dog)
    #         if current in group1 and dog in group1:
    #             return False
    #         elif current in group1 and dog not in group2:
    #             group2.append(dog)
    #         elif current in group2 and dog in group2:
    #             return False
    #         elif current in group2 and dog not in group1:
    #             group1.append(dog)
    #     if len(q) == 0:
    #         if len(puppies) != 0:
    #             q.append(puppies[0])
    # return True

#solution with stack
    group1 = []
    group2 = []
    puppies = list(dislikes.keys())
    group1.append(puppies[-1])
    while puppies:
        current = puppies.pop()
        if current not in group1 and current not in group2:
            group1.append(current)
        for dog in dislikes[current]:
            if dog not in group1 and dog not in group2:
                if dog in puppies:
                    puppies.remove(dog)
                    puppies.append(dog)
            if current in group1 and dog in group1:
                return False
            elif current in group1 and dog not in group2:
                group2.append(dog)
            elif current in group2 and dog in group2:
                return False
            elif current in group2 and dog not in group1:
                group1.append(dog)
    return True