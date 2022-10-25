# Can be used for BFS
from collections import deque
from dis import dis 

def possible_bipartition(dislikes):

    # Empty list is partionable
    if dislikes == None:
        return True

    color = {}

    for dog in dislikes:
        if dog in color:
            # Already processed
            continue

        q = deque()
        q.append(dog)
        color[dog] = 0
        print(color)

        while (len(q) > 0):
            dog = q.popleft()
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
                    print(color)
    return True

