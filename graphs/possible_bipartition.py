            
dislikes = {
            "Fido": [],
            "Nala": ["Cooper", "Spot"],
            "Cooper": ["Nala", "Spot"],
            "Spot": ["Nala", "Cooper"]
            }

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """

    dog_groups = {}
    for dog in dislikes:
        if dog not in dog_groups:
            stack = [dog]
            dog_groups[dog] = 0
            while stack:
                dog = stack.pop()
                for name in dislikes[dog]:
                    if name not in dog_groups:
                        stack.append(name)
                        dog_groups[name] = 1 - dog_groups[dog]
                    elif dog_groups[name] == dog_groups[dog]:
                        return False
    return True

print(possible_bipartition(dislikes))          
            



