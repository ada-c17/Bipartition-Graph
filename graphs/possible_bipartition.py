def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ? -> no idea, not great
        Space Complexity: ?-> O(n)
    """
    #guard clause
    n = len(dislikes)
    if n == 0 or n == 1:
        return True

    #dictionary to store group assignment/coloring
    #if none-> no assigment to a group, otherwise, "group1" or "group2" assigned
    #loop through adj. dict to create new dict with default of none values for dogs to start

    fight_group = {}
    for dog in dislikes:
        fight_group[dog] = None
    
    fight_group_values = fight_group.values()

    #account for case if where not all nodes visited-> aka an isolated dog or clusters of dogs 
    while not all(fight_group_values):
        dog_queue = []
        for dog in fight_group:
            if fight_group[dog] == None:
                #I think hard coding to grp1 works- this would be for an isolated dog or group of dog nodes?
                fight_group[dog] = "group1"
                dog_queue.append(dog)
                break

        while dog_queue:
            current_dog = dog_queue.pop(0)
            #account for having or not having neighbors-> BFS
            for neighbor in dislikes[current_dog]:
                if fight_group[neighbor] == None:
                    if fight_group[current_dog] == "group1":
                            fight_group[neighbor] = "group2"
                    else:
                        fight_group[neighbor] = "group1"
                    dog_queue.append(neighbor)
                if fight_group[neighbor] == fight_group[current_dog]:
                    return False
    return True





