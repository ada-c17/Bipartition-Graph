# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """

    if not dislikes:
        return True

    distanceMap = {dog: -1 for dog in dislikes}
    
    startDog = list(dislikes.keys())[0]
    distanceMap[startDog] = 0
    queue = deque([startDog])
    visitedDogs = set()

    while queue:
        curDog = queue.popleft()
        visitedDogs.add(curDog)

        for opp in dislikes[curDog]:
            if distanceMap[opp] == -1:
                distanceMap[opp] = distanceMap[curDog] + 1
                queue.append(opp)
            elif distanceMap[opp] == distanceMap[curDog]:
                return False
        
        if not queue:
            for dog in dislikes:
                if dog not in visitedDogs:
                    queue.append(dog)
                    break

    return True