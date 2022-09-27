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
        Time Complexity: O(E) checking every edge until it identifies a cycle or has checked every edge without finding one.
        Space Complexity: O(E) as it puts a new call with all associated data storage onto the stack for every edge it has to check.
    """
    for dog in dislikes:
        seen = []
        if not check_enemies(dislikes, dog, seen, None):
            return False
    return True

