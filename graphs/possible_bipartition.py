# Can be used for BFS
from collections import deque 

def possible_bipartition_helper(start_dog, dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    

    pen_a = set()
    pen_b = set()
    pen_a.add(start_dog)
    queue = deque([start_dog])

    while queue:
        dog = queue.popleft()
        visited = pen_a.union(pen_b)

        for bad_dog in dislikes[dog]:
            pen = pen_b if dog in pen_a else pen_a
            if bad_dog in visited and bad_dog not in pen:
                return False
            if bad_dog not in visited:
                pen.add(bad_dog)
                queue.append(bad_dog)
    
    new_dislikes = {dog: dislikes[dog] for dog in dislikes if dog not in pen_a.union(pen_b)}
    if new_dislikes:
        start_dog = next(iter(new_dislikes))
        return possible_bipartition_helper(start_dog, new_dislikes)
    return True

def possible_bipartition(dislikes):
    if len(dislikes) in {0, 1}:
        return True
    start_dog = next(iter(dislikes))
    result = possible_bipartition_helper(start_dog, dislikes)
    return result