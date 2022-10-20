def is_group_an_option(group, graph, dog):
    for disliked in graph[dog]:
        if disliked in group:
            return False
    return True

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    
    dog_list = list(dislikes.keys())
    if len(dog_list) <= 2:
        return True
    
    group_1 = set()
    group_2 = set()
    sorted = set()

    while dog_list:
        current = dog_list.pop()
        if current in sorted:
            continue
        print(current)
        if is_group_an_option(group_1, dislikes, current):
            group_1.add(current)
            sorted.add(current)
            print(current + " added to group 1")
        elif is_group_an_option(group_2, dislikes, current):
            group_2.add(current)
            sorted.add(current)
            print(current + " added to group 2")
        else:
            print(current + "cannot be added to either group")
            group_1_problems = list(group_1.intersection(set(dislikes[current])))
            # print("problems with group 1: " + str(group_1_problems))
            groupable = True
            for dog in group_1_problems:
                if is_group_an_option(group_2, dislikes, dog):
                    group_1.remove(dog)
                    group_2.add(dog)
                    print(dog + " removed from group 1 and added to group 2")
                else:
                    groupable = False
                    print("cannot move " + dog)

            if groupable:
                sorted.add(current)
                group_1.add(current)
                print(current + " can now be added to group 1")
            else:
                groupable = True
                group_2_problems = list(group_2.intersection(set(dislikes[current])))
                # print("problems with group 2: " + group_2_problems)
                for dog in group_2_problems:
                    if is_group_an_option(group_1, dislikes, dog):
                        group_2.remove(dog)
                        group_1.add(dog)
                        print(dog + " moved to group 1")
                    else:
                        groupable = False
                        print(dog + " can't be moved to group 1")
                if groupable:
                    sorted.add(current)
                    group_2.add(current)
                    print(dog + " moved to group 2")
                else:
                    print("can't sort; returning False")
                    return False
            
    return True