# The graph is stored in an adjacency dictionary where each key
# represents an item in the graph and each value in the dictionary
# corresponds to a list of edges from the key

# Can be used for BFS: from collections import deque
def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    if dislikes == {}:
        return True
    grouped_dogs = {dog: 'TBD' for dog in dislikes} 

    # BFS:
    dogs_visited = set()
    dog_list = [dog for dog in dislikes]
    start_dog = dog_list[-1]

    grouped_dogs[start_dog] = 'group A'
    queue = [start_dog]  # FIFO

    while len(dogs_visited) != len(dislikes): # this is for when run into dog with no neighbors/edges
        while queue:
            current_dog = queue.pop(-1) 
            dogs_visited.add(current_dog)
            if current_dog in dog_list:
                dog_list.remove(current_dog)
            for foe_dog in dislikes[current_dog]: 
                if grouped_dogs[foe_dog] == 'TBD':
                    if grouped_dogs[current_dog] == 'group A':
                        grouped_dogs[foe_dog] = 'group B'
                    else:
                        grouped_dogs[foe_dog] = 'group A'
                if grouped_dogs[foe_dog] == grouped_dogs[current_dog]:
                    return False

                if foe_dog not in dogs_visited:
                    queue.append(foe_dog)
        
            if not queue and len(dog_list) != 0:
                next_dog = dog_list.pop()
                queue.append(next_dog)
    return True



