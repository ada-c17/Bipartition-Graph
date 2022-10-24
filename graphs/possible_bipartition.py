def bipartition_helper(visited, dislikes, dog, current):
    visited.add(dog)
    for enemy in dislikes[dog]:
        if enemy not in visited:
            return bipartition_helper(visited, dislikes, enemy, dog)
        else:
            if enemy != current:
                return False

    return True


def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(n2)
        Space Complexity: O(n)
    """
    pass
    if len(dislikes) < 2:
        return True

    for dog, enemy in dislikes.items():
        if enemy:
            visited = set()
            if not bipartition_helper(visited, dislikes, dog, None):
                return False

    return True

# brute force soultion below only works if graph is connected

# def possible_bipartition(dislikes):
#     """ Will return True or False if the given graph
#         can be bipartitioned without neighboring nodes put
#         into the same partition.
#         Time Complexity: O(n3)
#         Space Complexity: O(n)
#     """
#     if len(dislikes) < 2:
#         return True

#     group1 = []
#     group2 = []

#     dogs = list(dislikes.keys())
#     start_node = dogs[0]

#     visited = [start_node]
#     queue = [start_node]

#     while len(queue) != 0:
#         current = queue.pop(0)

#         if len(dislikes[current]) == 0:
#             group1.append(current)
#             if len(queue) == 0:
#                 current_index = dogs.index(current)
#                 queue.append(dogs[current_index + 1])

#         for enemy in dislikes[current]:
#             # an enemy of current doesn't dislike current
#             if current not in dislikes[enemy]:
#                 return False

#             if enemy not in visited:
#                 visited.append(enemy)
#                 queue.append(enemy)

#             if current not in group1 and current not in group2:
#                 if enemy not in group1:
#                     group1.append(current)
#                 elif enemy not in group2:
#                     group2.append(current)
#             elif current in group1 and enemy in group1:
#                 return False
#             elif current in group2 and enemy in group2:
#                 return False

#     return True
