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
    first = list(dislikes.keys())[0]
    all_nodes = set(list(dislikes.keys()))
    stack = []
    group1 = set()
    group2 = set()
    visited = set()
    stack.append(first)
    group1.add(first)

    while stack: 
        current = stack.pop(0)
        visited.add(current)
        current_group = group1 if current in group1 else group2
        other_group = group2 if current_group is group1 else group1
        for neighbor in dislikes[current]: 
            if neighbor not in visited:
                stack.append(neighbor)
            if neighbor in current_group:
                return False
            other_group.add(neighbor)

        #handle disconnected graphs
        if (not stack) and (len(visited) != len(all_nodes)):
            for node in all_nodes:
                if node not in visited:
                    stack.append(node)
                    print(stack)
                    break
    return True

