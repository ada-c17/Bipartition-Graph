# Can be used for BFS
from collections import deque


def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """

    if not dislikes:
        return True

    first_dog = list(dislikes.keys())[0]

    q = deque([first_dog])
    v = []
    safe_rooms = {}
    for key in dislikes.keys():
        safe_rooms[key] = 0

    safe_rooms[first_dog] = 1

    for dog in dislikes:
        while q:
            current = q.popleft()
            v.append(current)
            if dislikes[current]:
                for rival in dislikes[current]:
                    if safe_rooms[rival] == 0:
                        safe_rooms[rival] = safe_rooms[current] + 1
                        q.append(rival)
                    else:
                        if safe_rooms[rival] == safe_rooms[current]:
                            return False
        if dog not in v:
            q.append(dog)

    return True


dislikes = {
    "Fido": ["Alfie", "Bruno"],
    "Rufus": ["James", "Scruffy"],
    "James": ["Rufus", "Alfie"],
    "Alfie": ["Fido", "James", "T-Bone"],
    "T-Bone": ["Alfie", "Scruffy"],
    "Scruffy": ["Rufus", "T-Bone"],
    "Bruno": ["Fido"]
}

possible_bipartition(dislikes)
