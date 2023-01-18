# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    if len(dislikes) == 0:
        return True

    groups = {key: 0 for key in dislikes.keys()}

    first_dog = list(dislikes.keys())[0]
    groups[first_dog] = 1
    queue = deque([first_dog])
    visited = set()

    while queue:
        current = queue.popleft()
        visited.add(current)

        if dislikes[current]:
            for disliked_dog in dislikes[current]:
                if groups[disliked_dog] == 0:
                    groups[disliked_dog] = groups[current] + 1
                    queue.append(disliked_dog)
                else:
                    if groups[disliked_dog] == groups[current]:
                        return False

    for dog in dislikes.keys():
        if dog not in visited:
            queue.append(dog)
            groups[dog] = 1
            while queue:
                current = queue.popleft()
                visited.add(current)
                for disliked_dog in dislikes[current]:
                    if disliked_dog not in visited:
                        queue.append(disliked_dog)
                        groups[disliked_dog] = groups[current] + 1
                    else:
                        if groups[disliked_dog] == groups[current]:
                            return False
    return True


    # Arrange
dislikes = {
    "Fido": [],
    "Rufus": ["James", "Alfie"],
    "James": ["Rufus", "T-Bone"],
    "Alfie": ["Rufus"],
    "T-Bone": ["James"]
}

    # Act
print(possible_bipartition(dislikes))

