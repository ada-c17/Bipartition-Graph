# Can be used for BFS
from collections import deque 
        
def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    queue = deque()
    dog_partitions = {}
    for dog in dislikes:
        if dog not in dog_partitions:
            dog_partitions[dog] = 0
            queue.append(dog)
        while queue:
            current_dog = queue.popleft()
            for neighbor in dislikes[current_dog]:
                if neighbor not in dog_partitions:
                    dog_partitions[neighbor] = 1 - dog_partitions[current_dog]
                    queue.append(neighbor)
                elif dog_partitions[neighbor] == dog_partitions[current_dog]:
                    return False
    return True
    

