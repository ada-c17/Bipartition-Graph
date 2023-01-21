# Can be used for BFS
from collections import deque

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N + E)
        Space Complexity: O(N)
    """
    visited = {}

    def dfs(dog, group):
        if dog in visited:
            return visited[dog] == group
        visited[dog] = group
        for neighbor in dislikes.get(dog, []):
            if not dfs(neighbor, not group):
                return False
        return True

    for dog in dislikes:
        if dog not in visited and not dfs(dog, True):
            return False
    return True

