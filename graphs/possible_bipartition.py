from collections import deque 


def possible_bipartition(dislikes):

    queue = deque([])
    dog_groups = {}

    for dog in dislikes.keys():
        if dog not in dog_groups and not queue:
            queue.append(dog)
            dog_groups = {dog: "group_1"}
        while queue:
            curr = queue.popleft()
            for neighbor in dislikes[curr]:
                if neighbor not in dog_groups:
                    if dog_groups[curr] == "group_1":
                        dog_groups[neighbor] = "group_2"
                    else:
                        dog_groups[neighbor] = "group_1"
                    queue.append(neighbor)
                else:
                    if dog_groups[neighbor] == dog_groups[curr]:
                        return False

    return True

