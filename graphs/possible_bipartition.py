# Can be used for BFS
from collections import deque

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    doggo = {}
    def dfs(dog):
        for dislikeDog in dislikes[dog]:
            if dislikeDog in doggo:
                if doggo[dislikeDog] == doggo[dog]:
                    return False
            else:
                doggo[dislikeDog] = 1 - doggo[dog]
                if not dfs(dislikeDog):
                    return False
        return True

    for dog in dislikes.keys():
        if dog not in doggo:
            doggo[dog] = 0
            if not dfs(dog):
                return False
    return True
