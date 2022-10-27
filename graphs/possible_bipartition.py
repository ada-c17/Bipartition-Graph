# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """

    # dog not in states - not discovered
    # states[dog] == 1 - dog is assigned group 1
    # states[dog] == 2 - dog is assigned group 2
    groups = {}

    for d in dislikes:
        print(d, dislikes[d])

    for dog in dislikes:
        if not dog in groups:
            q = []
            q.append(dog)
            groups[dog] = 1
            while len(q) > 0:
                current = q[0]
                q.pop(0)
                for neighbor in dislikes[current]:
                    if not neighbor in groups:
                        q.append(neighbor)
                        groups[neighbor] = 3 - groups[current]
                    elif groups[neighbor] == groups[current]:
                        return False

    return True

