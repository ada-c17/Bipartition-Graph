# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    dogs_dictionary = {i:None for i in dislikes.keys()}

    def dfs_helper(node):
    
    # for loop assigns dog to the dog group that it will be apart of 
        for dogs in dislikes[node]:
            # checks if dog has been assigned a group
            if dogs_dictionary[dogs]:
                # early return if there can not be bipartisan in the group

                if dogs_dictionary[node] == dogs_dictionary[dogs]:
                    return False
            else:
            # assigns dog to group or return false if
            # bipartisan is not possible
                dogs_dictionary[dogs] = 2 if dogs_dictionary[node] == 1 else 1
                if not dfs_helper(dogs):
                    return False
        return True
    
    # check if dog has not been assigned group
    # assign it to group 1
    # return false if dfs helper returns false    
    for dog in dislikes.keys():
        if not dogs_dictionary[dog]:
            dogs_dictionary[dog] = 1
        if not dfs_helper(dog):
            return False
    return True


