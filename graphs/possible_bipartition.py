# Can be used for BFS

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    grp1 = set()
    grp2 = set()
    visited = set()

    for dog in dislikes:
        if dog in visited:
            # already handled this dog
            continue

        q = [dog]
        grp1.add(dog)
        while q:
            parent_dog = q.pop(0)

            if parent_dog in grp1:
                parent_group = grp1
                child_group = grp2
            else:
                parent_group = grp2
                child_group = grp1

            for hated_dog in dislikes[parent_dog]:
                if hated_dog in parent_group:
                    return False
                else: 
                    child_group.add(hated_dog)
                    if hated_dog not in visited:
                        q.append(hated_dog)
                        
            visited.add(parent_dog)
    return True