# Can be used for BFS
from collections import deque 

# dislikes = {
#             "Fido": [],
#             "Nala": ["Cooper", "Spot"],
#             "Coooper": ["Nala", "Spot"],
#             "Spot": ["Nala", "Cooper"]
#             }

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    room_1 = []
    room_2 = []
    if dislikes:
        for dog in dislikes:
            if  dislikes[dog] == [] or room_1 == []:
                room_1.append(dog)
                print(f"added {dog} to room1")
                print(room_1)
            elif helper(dislikes[dog],room_1) == True:
                room_1.append(dog)
                print(f"added {dog} to room1")
                print(room_1)
            elif helper(dislikes[dog],room_2) == True:
                room_2.append(dog)
                print(f"added {dog} to room2")
                print(room_2)
            else:
                return False
        return True

def helper(list1, list2):
    for item in list1:
        if item in list2:
            return False
    return True