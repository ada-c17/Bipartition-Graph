# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    groups = {} 
    #  create list of all the dogs, arr of dogs 
    for dog in dislikes.keys(): 
        queue = deque()
        queue.append(dog)
        while queue: 
            current = queue.popleft()
            if current not in groups: 
                groups[current] = True 
            # grab the value for current dog 
            # this will be a list of all the dogs current dog can't be with 
            disliked_dogs = dislikes[current]
            for bad_dog in disliked_dogs: 
                if bad_dog not in groups:
                    # set the value to false for the dogs current dog
                    # cannot be paired with 
                    groups[bad_dog] = not groups[current]
                    # add current bad_dog to the queue 
                    queue.append(bad_dog)
                else: 
                    if groups[bad_dog] == groups[current]: 
                        return False 
    return True 
            


