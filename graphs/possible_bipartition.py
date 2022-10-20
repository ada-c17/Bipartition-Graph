def can_partition_dog(dog, dislikes_graph):
    dog_group = { dog: True }
    dog_list = [dog]
    partitioned = set()

    while dog_list:
        current_dog = dog_list.pop()
        if current_dog in partitioned: continue
        partitioned.add(current_dog)

        for disliked_dog in dislikes_graph[current_dog]:
            if (disliked_dog in dog_group) and (dog_group[current_dog] == dog_group[disliked_dog]):
                return False

            dog_group[disliked_dog] = not dog_group[current_dog]
            dog_list.append(disliked_dog)

    return True

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """

    if len(dislikes.keys()) <= 2:
        return True

    for dog in dislikes.keys():
        if not can_partition_dog(dog, dislikes):
            return False

    return True