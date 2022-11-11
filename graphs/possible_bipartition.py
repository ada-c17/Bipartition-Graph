# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N+E); N is the number of dogs & E is the number of dislikes
        Space Complexity: O(N); N is the number of dogs 
    """
    def can_partition_dog(picked_dog):
        dog_group = { picked_dog: True }
        to_visit = [picked_dog]
        visited = set()

        while len(to_visit) > 0:
            dog = to_visit.pop()
            if dog in visited: continue
            visited.add(dog)

            for other_dog in dislikes[dog]:
                if other_dog in dog_group and dog_group[dog] == dog_group[other_dog]:
                    return False

                dog_group[other_dog] = not dog_group[dog]
                to_visit.append(other_dog)

        return True

    for dog in dislikes.keys():
        if not can_partition_dog(dog):
            return False

    return True

