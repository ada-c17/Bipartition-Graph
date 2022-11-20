def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
    can be bipartitioned without neighboring nodes put
    into the same partition.
    Time Complexity: ?
    Space Complexity: ?
    """
    if len(dislikes) <= 2:
        return True

    visited = {dog : False for dog in dislikes.keys()}

    for dog in dislikes.keys():
        if not visited[dog]:
            queue = [dog]
        while queue:
            dog1 = queue.pop()
            for dog2 in dislikes[dog1]:
                if not visited[dog2]:
                    visited[dog2] = 2 if (visited[dog1] == 1) else 1
                    queue.append(dog2)
                elif visited[dog1] == visited[dog2]:
                    return False
    return True