# Can be used for BFS
from collections import deque


def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(dogs + edges) because I check them all at least once
        Space Complexity: O(dogs) because I made a set for checked, a list for queue, and the dictionary for coloring is also O(n)
    """

    if len(dislikes) == 0:
        return True

    checked = set()

    for first_dog in dislikes.keys():

        dog_to_color = {first_dog: 'red'}  # visited
        queue = [first_dog]

        while queue:
            dog = queue.pop(0)  # current dog
            checked.add(dog)

            color = 'red' if dog_to_color[dog] == 'blue' else 'blue'

            for neighbor in dislikes[dog]:
                if neighbor not in dog_to_color:
                    dog_to_color[neighbor] = color
                    queue.append(neighbor)
                elif dog_to_color[neighbor] != color:
                    return False

            # exit early if we already painted all the dogs
            if len(checked) == len(dislikes):
                return True

    return True
