# Can be used for BFS
from collections import deque

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    partition_1 = set()
    partition_2 = set()
    q = deque(dislikes)
    
    for i in range(len(q)):
        if q[i] in partition_1 or q[i] in partition_2:
            continue
        queue = deque()
        queue.append(q[i])
        partition = "1"
        while queue:
            for i in range(len(queue)):
                dog = queue.popleft()
                print(dog, i)
                if partition == "1":
                    if dog in partition_2:
                        return False
                    partition_1.add(dog)
                
                if partition == "2":
                    if dog in partition_1:
                        return False
                    partition_2.add(dog)

                for dislike in dislikes[dog]:
                    if dislike not in partition_1 and dislike not in partition_2:
                        queue.append(dislike)
                        
            if partition == "1":
                partition = "2"
            else:
                partition = "1"

    return True



test_1 = {
    "Fido": [],
    "Rufus": ["James", "Scruffy"],
    "James": ["Rufus", "Alfie"],
    "Alfie": ["Rufus", "T-Bone"],
    "T-Bone": ["Alfie", "Scruffy"],
    "Scruffy": ["Rufus", "T-Bone"]
}

test_2 = {
    "Fido": ["Alfie", "Bruno"],
    "Rufus": ["James", "Scruffy"],
    "James": ["Rufus", "Alfie"],
    "Alfie": ["Fido", "James"],
    "T-Bone": ["Scruffy"],
    "Scruffy": ["Rufus", "T-Bone"],
    "Bruno": ["Fido"]
}

# print(possible_bipartition(test_2))