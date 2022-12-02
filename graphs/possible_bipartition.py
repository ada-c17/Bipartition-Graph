# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    if not dislikes:
        return True

    set1 = set()  # first group of dogs
    set2 = set()  # second group of dogs
    set_visited = set()  # putting it to a set to minimize the time complexity O(1) for the look-up
    queue = []

    for current_dog in dislikes:
        set1.add(current_dog)  # put all dogs in the same group first

    current_dog = list(dislikes.keys())[0]
    queue.append(current_dog)

    for dog in dislikes:
        while queue:
            current_dog = queue.pop(0)
            set_visited.add(current_dog)
            if dislikes[current_dog]:
                if current_dog in set1:
                    for enemy in dislikes[
                        current_dog]:  # checking for enemies of the dog
                        if enemy not in set2 and enemy not in set_visited:  # if this is the first time we see this enemy
                            # it is still in our set1 and we need to move it to set2
                            set1.remove(
                                enemy)  # and delete it from set1 accordingly
                            set2.add(enemy)
                            queue.append(enemy)
                elif current_dog in set2:  # if it's in set2, it means we have already moved it here
                    if dislikes[current_dog]:
                        for enemy in dislikes[current_dog]:
                            if enemy not in set1:
                                # if the enemy is not in set1, it means we
                                # have already moved it to set2
                                return False
                            elif enemy not in set_visited:
                                queue.append(enemy)
        if dog not in set_visited:
            queue.append(dog)
    return True





