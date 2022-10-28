# Can be used for BFS
from collections import deque


def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    groups = {}

    def dfs(dog, group):
        if dog in groups:
            return False if groups[dog] != group else True

        groups[dog] = group
        dislikeGroup = 1 if group == 2 else 2
        for dislikeDog in dislikes[dog]:
            if not dfs(dislikeDog, dislikeGroup):
                return False
        return True

    for dog in dislikes:
        if dog not in groups:
            if not dfs(dog, 1):
                return False
    return True
