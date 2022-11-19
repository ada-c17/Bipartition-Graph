# Can be used for BFS
from collections import deque 


def possible_bipartition(dislikes):
    if len(dislikes) <= 2:
        return True

    visited = {}
    for dog in dislikes.keys():
        visited[dog] = False
    
    for dog in visited.keys():
        queue = [dog]
        while queue:
            dog1 = queue.pop()
            for dog2 in dislikes[dog1]:
                if not visited[dog2]:
                    visited[dog2] = 2 if (visited[dog1] == 1) else 1
                    queue.append(dog2)
                else:
                    if visited[dog1] == visited[dog2]:
                        return False
    return True