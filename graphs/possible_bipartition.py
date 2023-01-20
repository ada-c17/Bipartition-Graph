# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N + E)
        Space Complexity: O(N + E)
    """
    if not dislikes: # check if the input is valid
        return True
    # Initialize the graph
    # Initialize the graph
    graph = {}

    for dog in dislikes:
        graph[dog] = []
    for dog, consumes in dislikes.items():
        for c in consumes:
            graph[dog].append(c)
            graph[c].append(dog)

    # Initialize the visited dictionary
    visited = {}
    for dog in graph:
        visited[dog] = -1

    # Use BFS traversal
    for dog in graph:
        if visited[dog] == -1:
            visited[dog] = 0
            queue = deque([dog])
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = 1 - visited[current]
                        queue.append(neighbor)
                    elif visited[neighbor] == visited[current]:
                        return False
    return True
