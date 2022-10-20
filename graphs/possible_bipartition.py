# Can be used for BFS
# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
        https://github.com/ada-c17/Bipartition-Graph
    """


    if not dislikes or len(dislikes) == 1:
            return True
            
        
    group_one = set()
    group_two = set()
    dog_visited = set()

    for dog in dislikes:
        if dog not in group_one and dog  not in group_two and dog  not in dog_visited:
            group_one.add(dog)
            dog_visited.add(dog)
            
        current_dog_is_group_one= dog in group_one
        
        for disliked in dislikes[dog]:
            if current_dog_is_group_one and disliked not in dog_visited:
                group_two.add(disliked)  
            elif disliked not in dog_visited: 
                group_one.add(disliked)
            if disliked in group_one and current_dog_is_group_one:
                return False

            elif disliked in group_two and not current_dog_is_group_one:
                return False

            dog_visited.add(disliked)  
    return True