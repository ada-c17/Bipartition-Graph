# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """

    if dislikes == None:
        return True

    color = {}

    for dog in dislikes:
        if dog in color:
            continue

        q = deque()
        q.append(dog)
        color[dog] = 0

        while (len(q) > 0):
            dog = q.pop()
            current_color = color[dog]
            fight_set = dislikes[dog]
            for fight_dog in fight_set:
                if fight_dog in color:
                    if color[fight_dog] == current_color:
                        return False
                else:
                    if current_color == 0:
                        next_color = 1
                    else:
                        next_color = 0
                    color[fight_dog] = next_color
                    q.append(fight_dog)
    return True


