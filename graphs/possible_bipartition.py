# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    color = {key: -1 for key in dislikes}

    def is_bipartite(key):
        color[key] = 1
        queue = deque([key])
        while queue:
            node = queue.popleft()
            for hater in dislikes[node]:
                if color[hater] == color[node]:
                    return False
                if color[hater] == -1:
                    color[hater] = 1 - color[node]
                    queue.append(hater)
        return True

    for key in dislikes:
        if color[key] == -1:
            if not is_bipartite(key):
                return False
    return True 
