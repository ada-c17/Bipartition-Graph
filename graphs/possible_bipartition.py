def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    dogs = {}

    def dfs(dog):
        for sad_dog in dislikes[dog]:
            if sad_dog in dogs: 
                if dogs[sad_dog] == dogs[dog]:
                    return False
            else:
                dogs[sad_dog] = 1 - dogs[dog]
                if not dfs(sad_dog):
                    return False
        return True
    
    for dog in dislikes.keys():
        if dog not in dogs:
            dogs[dog] = 0
            if not dfs(dog):
                return False
    return True 

