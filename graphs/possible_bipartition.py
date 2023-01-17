from collections import deque 

def possible_bipartition(dislikes):
    
    if not dislikes:
        return True

    dogs = {dog: -1 for dog in dislikes.keys()}

    def breadth_first(start):
        dogs[start]
        q = deque()
        q.append(start)

        while q:
            curr = q.popleft()
            for node in dislikes[curr]:

                if dogs[node] == -1:
                    dogs[node] = 1 - dogs[curr]
                    q.append(node)

                elif dogs[node] == dogs[curr]:
                    return False

        return True

    for dog in dislikes.keys():

        if dogs[dog] == -1:
            if not breadth_first(dog):
                return False

    return True

