def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    groups = {
        1: [],
        2: []
    }

    visited = []
    queue = []

    for dog in dislikes:
        if dog not in visited:
            visited.append(dog)
            queue.append(dog)

        while queue:
            doggo = queue[0]
            group_one_possible = True
            group_two_possible = True

            for neighbor in dislikes[doggo]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
                elif neighbor in groups[1]:
                    group_one_possible = False
                elif neighbor in groups[2]:
                    group_two_possible = False

                # Ensure all edges mapped in adjacency dict
                if doggo not in dislikes[neighbor]:
                    dislikes[neighbor].append(doggo)

            if group_one_possible:
                groups[1].append(doggo)
            elif group_two_possible and not group_one_possible:
                groups[2].append(doggo)
            else:
                return False
            queue.pop(0)

    print(groups)

    return True

dislikes = {
    "Fido": [],
    "Rufus": ["James", "Scruffy"],
    "James": ["Rufus", "Alfie"],
    "Alfie": ["Rufus", "T-Bone"],
    "T-Bone": ["Alfie", "Scruffy"],
    "Scruffy": ["Rufus", "T-Bone"]
}
answer = possible_bipartition(dislikes)
print(answer)