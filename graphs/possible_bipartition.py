# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """

    visited_nodes = {}
    queue = []

    # Iterate through the keys in dislikes
    for dog in dislikes.keys():
        if dog not in visited_nodes:
            queue.append(dog)
            visited_nodes[dog] = 0

        while queue:
            current = queue.pop(0)

            # Iterate through the neighbors of current node
            for neighbor in dislikes[current]:
                if neighbor not in visited_nodes:
                    queue.append(neighbor)
                    visited_nodes[neighbor] = visited_nodes[current] + 1
                elif visited_nodes[neighbor] == visited_nodes[current]:
                    return False

    return True
                