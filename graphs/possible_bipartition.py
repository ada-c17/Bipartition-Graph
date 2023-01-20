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
    group = {}
    for key in dislikes.keys():
        group[key] = 0

    group[first_dog] = 1

    for dog in dislikes:
        while q:
            current = q.popleft()
            v.append(current)
            if dislikes[current]:
                for other_dog in dislikes[current]:
                    if group[other_dog] == 0:
                        group[other_dog] = group[current] + 1
                        q.append(other_dog)
                    else:
                        if group[other_dog] == group[current]:
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

