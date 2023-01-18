# Can be used for BFS
from collections import deque


def possible_bipartition(dislikes_dict):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """

    # return true if the graph is empty
    if not dislikes_dict:
        return True

    graph = {}
    for node in dislikes_dict:
        graph[node] = dislikes_dict[node]

    color = {}
    for node in graph:
        # check if the node has been visited
        if node not in color:
            # assign a color to the current node
            color[node] = 0
            queue = deque([node])
            while queue:
                # get the next node to visit
                current = queue.popleft()
                # visit the neighbors of the current node
                for neighbor in graph[current]:
                    if neighbor not in color:
                        # assign the opposite color to the neighbor
                        color[neighbor] = 1 - color[current]
                        queue.append(neighbor)
                    elif color[neighbor] == color[current]:
                        # if the neighbor already has the same color as the current node, the graph is not bipartite
                        return False
    return True
