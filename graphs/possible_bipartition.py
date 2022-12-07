# Can be used for BFS
from collections import deque 

def create_dict(adj_list):
    helper_dict = {}
    for ele in adj_list:
        helper_dict[ele] = None
    return helper_dict

def possible_bipartition(dislikes):
    """ 
    Will return True or False if the given graph can be bipartitioned 
    without neighboring nodes put into the same partition.
    Time Complexity: ?
    Space Complexity: ?
    """
    if not dislikes:
        return True

    doggo_dict = create_dict(dislikes)

    for doggo in dislikes:
        if not doggo_dict[doggo]:
            if not bfs(doggo, doggo_dict, dislikes):
                return False
    return True

def bfs(doggo, doggo_dict, dislikes):
    queue = deque()
    queue.append(doggo)
    doggo_dict[doggo] = 1

    while queue:
        curr = queue.popleft()

        for dog in dislikes[curr]:
            if doggo_dict[dog] == doggo_dict[curr]:
                return False
            if not doggo_dict[dog]:
                doggo_dict[dog] = 2 if doggo_dict[curr] == 1 else 1
                queue.append(dog)
    return True

