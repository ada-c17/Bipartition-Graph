# Can be used for BFS
from collections import deque 

def partition_subgraph(dislikes, start_dog):
    first_dog = start_dog
    all_dogs = {first_dog: True}
    dog_queue = deque([first_dog])
    while dog_queue:
        dog = dog_queue.popleft()
        dog_bool = all_dogs[dog]
        for rival_dog in dislikes[dog]:
            if rival_dog not in all_dogs:
                all_dogs[rival_dog] = not dog_bool
                dog_queue.append(rival_dog)
            elif all_dogs[rival_dog] == dog_bool:
                return False
    return set(all_dogs.keys())

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    if not dislikes or len(dislikes) < 3:
        return True
    partitioned_dogs = set()
    for dog in dislikes:
        if dog not in partitioned_dogs:
            dogs_to_partition = partition_subgraph(dislikes, dog)
            if not dogs_to_partition:
                return False
            else: 
                partitioned_dogs.update(dogs_to_partition)
    return True


