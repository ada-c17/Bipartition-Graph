# Can be used for BFS
from collections import deque 
global color
def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
        dislikes = { 
            "Fido": [],
            "Nala": ["Cooper", "Spot"],
            "Cooper": ["Nala", "Bruno"],
            "Spot": ["Nala"],
            "Bruno": ["Cooper"]
            }
        At the first loop we’re going to initiate all nodes with group 01 value. At the second loop for every node that has the group 01 value we’re going to check its neighbors and, if possible, set it a different group value.   
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

