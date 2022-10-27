# Can be used for BFS
from collections import deque 


def bipartition_helper(visited, dislikes, dog, hater):
    visited.add(dog)
    for ddog in dislikes[dog]:
        if ddog not in visited:
            return bipartition_helper(visited, dislikes, ddog, dog)
        else:
            if ddog != hater:
                return False

    return True


def possible_bipartition(dislikes):
    if len(dislikes) == 0:
        return True

    for dog, ddog in dislikes.items():
        if ddog:
            visited = set()
            if not bipartition_helper(visited, dislikes, dog, None):
                return False

    return True