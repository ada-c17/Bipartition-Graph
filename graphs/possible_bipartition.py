# Can be used for BFS
from collections import deque 

def try_to_add(dislikes, dog, group):
    for doggie in group:
        if dog in dislikes[doggie]:
            return False
        if doggie in dislikes[dog]:
            return False
    group.append(dog)
    return True

def recursive_check_and_place(all_dogs, dislikes, check, group1, group2):
    '''
    Each member of check is a tuple with dog name at index 0 and group to add at index 1
    '''
    if not check:
        return True
    
    curr = check.pop()
    group_num = curr[1]
    dog_name = curr[0]
    if group_num == 1:
        group = group1
    else:
        group = group2
    if not try_to_add(dislikes, dog_name, group):
        return False
    neighbors = dislikes[dog_name]
    if group_num == 1:
        neighbor_group_num = 2
    else:
        neighbor_group_num = 1
    for neighbor in neighbors:
        if neighbor in all_dogs:
            all_dogs.remove(neighbor)
            check.append((neighbor, neighbor_group_num))
    return recursive_check_and_place(all_dogs, dislikes, check, group1, group2)

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    all_dogs = list(dislikes.keys())
    group1 = []
    group2 = []
    check = []

    while all_dogs:
        first_dog = all_dogs.pop()
        group1.append(first_dog)
        neighbors = dislikes[first_dog]
        for neighbor in neighbors:
            all_dogs.remove(neighbor)
            check.append((neighbor, 2))
        if not recursive_check_and_place(all_dogs, dislikes, check, group1, group2):
            return False
    
    return True
    