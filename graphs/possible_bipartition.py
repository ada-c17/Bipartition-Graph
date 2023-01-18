# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    group_1 = []
    group_2 = []

    def bfs(dog):
        current_dog = dog in group_1

        for dog_neighbor in dislikes[dog]:
            if dog_neighbor not in group_1 and dog_neighbor not in group_2:
                if current_dog:
                    group_2.append(dog_neighbor)
                else:
                    group_1.append(dog_neighbor)

                if not bfs(dog_neighbor):
                    return False

            if dog_neighbor in group_1:
                if current_dog:
                    return False

            if dog_neighbor in group_2:
                if not current_dog:
                    return False
    
        return True

    for dog in dislikes:
            if dog not in group_1 and dog not in group_2:
                group_1.append(dog)

                result = bfs(dog)

                if not result:
                    return False

    return True
                

    