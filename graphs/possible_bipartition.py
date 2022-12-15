# Can be used for BFS
from collections import deque
import queue 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N)
        Space Complexity: O(N)
    """
    if not dislikes or len(dislikes) < 3:
        return True

    chains = {}

    for dog in dislikes:
        if dog not in chains:
            line = []

            line.append(dog)

            chains[dog] = 1

            while len(line) > 0:
                current_pup = line[0]
                line.pop(0)
                for enemy in dislikes[current_pup]:

                    if enemy not in chains:

                        line.append(enemy)
                        chains[enemy] = 1 - chains[current_pup]

                    elif chains[current_pup] == chains[enemy]:
                        return False

    return True