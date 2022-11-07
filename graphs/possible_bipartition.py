# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes: dict) -> bool:
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    if not dislikes:
        return True
    
    colors = {dog: -1 for dog in dislikes.keys()}

    def bfs(start):
        colors[start]
        queue = deque()
        queue.append(start)
        
        while queue:
            current = queue.popleft()
            for node in dislikes[current]:
                if colors[node] == -1:
                    colors[node] = 1 - colors[current]
                    queue.append(node)
                else:
                    if colors[node] == colors[current]:
                        return False
        return True

    for dog in dislikes.keys():
        if colors[dog] == -1:
            if bfs(dog) is False:
                return False

    return True