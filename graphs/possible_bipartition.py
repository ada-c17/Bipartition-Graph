def check_enemies(dislikes, dog, seen, parent):
    seen.append(dog)
    for enemy in dislikes[dog]:
        if enemy not in seen:
            return check_enemies(dislikes, enemy, seen, dog)
        else:
            if enemy != parent:
                return False

    return True

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    for dog in dislikes:
        seen = []
        if not check_enemies(dislikes, dog, seen, None):
            return False
    return True
