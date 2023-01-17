# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    # BFS solution
    if len(dislikes) == 0:
        return True


    def start_new_queue(dislikes, visited):
        first_item = list(dislikes.keys())[0]
        visited[first_item] = 0
        return [first_item]

    visited = {}
    queue = start_new_queue(dislikes, visited)

    while queue:
        current = queue.pop(0)
        curr_color = visited[current]
        for nbr in dislikes[current]:
            if nbr not in visited:
                visited[nbr] = 1 if curr_color == 0 else 0
                queue.append(nbr)
            else:
                if curr_color == visited[nbr]:
                    return False
        if len(queue) == 0 and len(visited) < len(dislikes):
            new_dislikes = {}
            for key, value in dislikes.items():
                if key not in visited:
                    new_dislikes[key] = value
            dislikes = new_dislikes
            queue = start_new_queue(dislikes, visited)
    return True

