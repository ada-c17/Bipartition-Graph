def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    seen = {}
    current_color = 1

    for dog in dislikes.keys():
        if not seen.get(dog):
            seen[dog] = current_color

            if not dfs(dislikes, dog, seen, current_color):
                return False

    return True

def dfs(dislikes, current_node, seen, current_color):
    neighbors = dislikes[current_node]

    for neighbor in neighbors:
        color = seen.get(neighbor)

        if not color:
            seen[neighbor] = -current_color
            if not dfs(dislikes, neighbor, seen, -current_color):
                return False
        elif color != -current_color:
            return False

    return True

