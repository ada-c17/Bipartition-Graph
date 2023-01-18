# Can be used for BFS
from collections import defaultdict, deque 

def possible_bipartition(dislikes):
    """ 
    Will return True or False if the given graph
    can be bipartitioned without neighboring nodes put
    into the same partition.
    Time Complexity: O(N)^2
    Space Complexity: O(N)

    Example -
    input: 
        dislikes = { 
            "Fido": [],
            "Nala": ["Cooper", "Spot"],
            "Cooper": ["Nala", "Bruno"],
            "Spot": ["Nala"],
            "Bruno": ["Cooper"]
            }
    output: 
        True
    """
    # 
    if len(dislikes) == 0:
        return True

    play_area = {}
    stack = []

    for dog in dislikes:
        # assign unassigned dog to play area + add to stack
        if dog not in play_area: 
            stack.append(dog)
            play_area[dog] = 0
            # look at stack and check neighbors
            while stack:
                current = stack.pop()
                # assign neighbors to group 
                for neighbor in dislikes[current]:
                    if neighbor not in play_area:
                        stack.append(neighbor)
                        play_area[neighbor] = 1 - play_area[current]
                    elif play_area[neighbor] == play_area[current]:
                        return False

    return True

