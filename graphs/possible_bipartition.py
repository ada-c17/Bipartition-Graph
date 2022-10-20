# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N+E), where N is number of dogs and E is number of dislikes
        Space Complexity: O(N), where N is number of dogs 
    """

    def can_partition_dog(target_dog):
        # group dogs into True or False groups
        dog_group = { target_dog: True }
        to_visit = [target_dog]
        visited = set()

        while len(to_visit) > 0:
            dog = to_visit.pop() # precondition: dog already in dog_group
            if dog in visited: continue
            visited.add(dog)
            
            for other_dog in dislikes[dog]:
                if other_dog in dog_group and dog_group[dog] == dog_group[other_dog]:
                    # dogs dislike each other, so this can't work
                    return False

                dog_group[other_dog] = not dog_group[dog]
                to_visit.append(other_dog)
        
        return True

    for dog in dislikes.keys():
        if not can_partition_dog(dog):
            return False

    return True
