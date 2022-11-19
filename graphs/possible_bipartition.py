# Can be used for BFS
from collections import deque
from ssl import VERIFY_X509_STRICT 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    group = {}
    stack = []
    
    for dog in dislikes:
        if dog not in group: 
            stack.append(dog) 
            group[dog] = 0
            while stack:
                current_dog = stack.pop() 
                for neighbor in dislikes[current_dog]:
                    if neighbor not in group: 
                        stack.append(neighbor)
                        group[neighbor] = 1 - group[current_dog] 
                    elif group[neighbor] == group[current_dog]:
                        return False
    
    return True
    




