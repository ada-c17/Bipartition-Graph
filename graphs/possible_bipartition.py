# Can be used for BFS
from collections import deque 


# class Graph:
#     def __init__(self, nodes):
#         self.adjlist = []
#         self.nodes = nodes

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    ## input: dislikes dictionary:
        ## dog names are key: [list of dogs that do not get along]
    ## output: True or False
        ## true if it is possible to split dogs into two groups
        ## false if it is not possible

    ## goal: create a graph with adjacency list
        ## navigate the graph through traversal
    
    #dictionary of nodes and its edges is a graph!

    #store dogs names, store relationship, and check if they can be
        # added to a group
    # nodes with connected edges cannot
        # be added to to group together

## create a dictionary, keys of the dictionary are dogs names
## values of the dictionary are dogs who fight
    # dogs_dictionary = {}
    
    # num_dogs = len(dislikes)

    # for a,b in dislikes:
    #     dogs_dictionary[a].append(b)
    #     dogs_dictionary[b].append(a)
    
    dogs_dictionary = {i:None for i in dislikes.keys()}

    def dfs_helper(node, dog_friends):
        if not dogs_dictionary[node]:
            #mark the node of dog passed in search
            dogs_dictionary[node] = dog_friends
        # else:
        #     return dislikes[node] == dog_friends
    
        for dogs in dislikes[node]:
            if dogs_dictionary[dogs]:
                if dogs_dictionary[dogs] == dog_friends:
                    return False
            else:
                if not dfs_helper(dogs, 2 if dog_friends == 1 else 1):
                    return False
        return True
        
    for dog in dislikes.keys():
        if not dislikes[dog] and not dfs_helper(dog, 1):
            return False
    return True


