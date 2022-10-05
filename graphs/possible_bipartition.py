# Can be used for BFS
from collections import deque 

group_1 = []
group_2 = []

def add_dog(graph, dog):
    if dog not in group_1 and dog not in group_2:
        group_1.append(dog)
        for neighbor in graph[dog]:    
            if neighbor in group_1:
                group_1.remove(neighbor)
            if neighbor not in group_2 and dog not in group_2:
                group_2.append(neighbor)
        return True
    return False

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """       
    graph = dislikes

    if not graph:
        return True

    dog_list = list(graph.keys())
    length = len(dog_list)

    for dog in dog_list:    
        dog_added = add_dog(graph, dog)                   
    
    if len(group_1) + len(group_2) == length:
        return True
    return False

# Execution #

# Arrange
dislikes = {
    "Fido": ["Alfie"],
    "Rufus": ["James", "Scruffy"],
    "James": ["Rufus", "Alfie"],
    "Alfie": ["Fido", "James"],
    "T-Bone": [],
    "Scruffy": ["Rufus"],
    "Bruno": [],
    "Spot": ["Nala"],
    "Nala": ["Spot"]
}

# Act
answer = possible_bipartition(dislikes)

# Assert
if answer:
    print('Pass test_multiple_dogs_in_middle_dont_dislike_any_others')
else:
    print('Fail test_multiple_dogs_in_middle_dont_dislike_any_others')

# Arrange
dislikes = {
    "Fido": [],
    "Rufus": ["James", "Alfie"],
    "James": ["Rufus", "T-Bone"],
    "Alfie": ["Rufus"],
    "T-Bone": ["James"]
}

# Act
answer = possible_bipartition(dislikes)

# Assert
if answer:
    print('Pass test_example_1')
else:
    print('Fail test_example_1')

dislikes = {
    "Fido": [],
    "Rufus": ["James", "Alfie"],
    "James": ["Rufus", "Alfie"],
    "Alfie": ["Rufus", "James"]
}

# Act
answer = possible_bipartition(dislikes)

# Assert
if not answer:
    print('Pass test_example_2')
else:
    print('Fail test_example_2')


# Arrange
dislikes = {
    "Fido": [],
    "Rufus": ["James", "Scruffy"],
    "James": ["Rufus", "Alfie"],
    "Alfie": ["Rufus", "T-Bone"],
    "T-Bone": ["Alfie", "Scruffy"],
    "Scruffy": ["Rufus", "T-Bone"]
}

# Act
answer = possible_bipartition(dislikes)

# Assert
if not answer:
    print('Pass test_example_r')
else:
    print('Fail test_example_r')


# Arrange
dislikes = {
    "Fido": ["Alfie", "Bruno"],
    "Rufus": ["James", "Scruffy"],
    "James": ["Rufus", "Alfie"],
    "Alfie": ["Fido", "James"],
    "T-Bone": ["Scruffy"],
    "Scruffy": ["Rufus", "T-Bone"],
    "Bruno": ["Fido"]
}

# Act
answer = possible_bipartition(dislikes)

# Assert
if answer:
    print('Pass test_will_return_true_for_a_graph_which_can_be_bipartitioned')
else:
    print('Fail test_will_return_true_for_a_graph_which_can_be_bipartitioned')

answer = possible_bipartition({})
if answer:
    print('Pass test_will_return_true_for_empty_graph')
else:
    print('Fail test_will_return_true_for_empty_graph')