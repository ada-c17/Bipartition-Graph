# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N + E) where N represents the amount of nodes (i.e. dogs) and E represents the amount of edges (i.e. disliked dogs) in total from each of the nodes
        Space Complexity: O(N) where N represents the amount of nodes (i.e. dogs)
    """
    """
    EXAMPLE 1:
    dislikes = { 
        "Fido": [],
        "Nala": ["Cooper", "Spot"],
        "Cooper": ["Nala", "Bruno"],
        "Spot": ["Nala"],
        "Bruno": ["Cooper"]
        }

    TRUE 

    EXAMPLE 2:
    dislikes = {
        "Fido": [],
        "Nala": ["Cooper", "Spot"],
        "Coooper": ["Nala", "Spot"],
        "Spot": ["Nala", "Cooper"]
    }

    FALSE 
    """

    if not dislikes: 
        return True 

    # Initialize a dictionary to keep track of which group each dog belongs to
    # Set the first dog to be part of group 1, and the others as part of group 0
    groups = {}
    for dog in dislikes.keys():
        groups[dog] = 0 

    first_dog = list(dislikes.keys())[0]
    groups[first_dog] = 1

    # For BFS, initialize a queue with the first dog in it and a visited list
    queue = [first_dog]
    visited = []

    # For each dog (node), iterate through its neighbors/edges (disliked dogs)
    # If the disliked dog's group is 0, update its group to be the current dog's group - 1 (this part is a little confusing for me if whoever is reviewing can clarify?)
    # and add the disliked dog to the queue 
    # Otherwise, if the group for the current dog and the disliked dog is the same, immediately return false 
    # Add the dog to the visited list after going through its edges/disliked dogs
    # Return true at the end
    for dog in dislikes: 
        while queue:
            current_dog = queue.pop(0)
            visited.append(current_dog)

            if dislikes[current_dog]:
                for disliked_dog in dislikes[current_dog]:
                    if groups[disliked_dog] == 0:
                        groups[disliked_dog] = groups[current_dog] - 1 # this works regardless of if you subtract or add 1?
                        queue.append(disliked_dog)
                    else:
                        if groups[current_dog] == groups[disliked_dog]:
                            return False 
            
        if dog not in visited:
            queue.append(dog)

    return True 

