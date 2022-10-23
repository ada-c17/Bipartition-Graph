# Can be used for BFS
from collections import deque
from threading import currentThread 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    if not dislikes: 
        return True

    groups = {}
    # {'Fido': 0, 'Nala': 0, 'Cooper': 0, 'Spot': 0, 'Bruno': 0}
    for key in dislikes.keys():
        groups[key] = 0
    
    first_dog = list(dislikes.keys())[0]

    groups[first_dog] = 1
    queue = [first_dog]
    visited = []

    while queue:
        current_dog = queue.pop(0)
        visited.append(current_dog)

        if dislikes[current_dog]:
            for frenemie in dislikes[current_dog]:
                if groups[frenemie] == 0:
                    groups[frenemie] = groups[current_dog] + 1
                    queue.append(frenemie)
                else:
                    if groups[frenemie] == groups[current_dog]:
                        return False
        else:
            for dog in dislikes:
                if dog not in visited:
                    queue.append(dog)
    print(groups)
    return True


    # queue = [first_dog]
    # visited = []

    # for dog in dislikes:
    #     if dog not in visited:
    #         queue.append(dog)
    #         visited.append(dog)

    # for enemy in dislikes:
    #     print(dislikes[enemy])
    # while queue:
    #     current_dog = queue.pop(0)
    #     print('current dog: ', current_dog)

    #     for enemy in dislikes[dog]:
    #         print('frenemie: ', enemy)
    #         if enemy in groupA:
    #             groupB.append(enemy)
    #         groupA.append(enemy)

    # print(visited)

    # print(groupA, groupB)


dislikes = { 
            "Fido": [],
            "Nala": ["Cooper", "Spot"],
            "Cooper": ["Nala", "Bruno"],
            "Spot": ["Nala"],
            "Bruno": ["Cooper"]
            }

possible_bipartition(dislikes)

'''
returns true
dislikes = { 
            "Fido": [],
            "Nala": ["Cooper", "Spot"],
            "Cooper": ["Nala", "Bruno"],
            "Spot": ["Nala"],
            "Bruno": ["Cooper"]
            }


returns true
dislikes = {
    "Fido": ["Alfie", "Bruno"],
    "Rufus": ["James", "Scruffy"],
    "James": ["Rufus", "Alfie"],
    "Alfie": ["Fido", "James"],
    "T-Bone": ["Scruffy"],
    "Scruffy": ["Rufus", "T-Bone"],
    "Bruno": ["Fido"]
    }
'''
