# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    # create a dictionary to store value 0 and 1 to make dog and their dislike dog store different value
    color_graph = {}
    # make sure all nodes in dislike get check
    for node in dislikes.keys():
        # assign 0 for start node is not in color_graph
        if node not in color_graph:
            color_graph[node] = 0
            # skip else statement if dog don't have dislike dog
            if len(dislikes[node]) == 0:
                continue
            else:
                stack = [node]
                # use bfs for checking
                while stack:
                    curr_node = stack.pop()
                    for dislike_dog in dislikes[curr_node]:
                        if dislike_dog in color_graph and color_graph[dislike_dog] == color_graph[curr_node]:
                            return False
                        elif dislike_dog in color_graph and color_graph[dislike_dog] != color_graph[curr_node]:
                            continue
                        else:
                            # assign value for dislike dog if they not in color_graph and add it into queue
                            color_graph[dislike_dog] = (1 - color_graph[curr_node]) % 2
                            stack.append(dislike_dog)
    return True
    

