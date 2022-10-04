# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    if len(dislikes) == 0:
        return True
    
    visited = {}
    queue = start_new_queue(dislikes, visited)
        
    while queue:
        current = queue.pop(0)
        curr_color = visited[current]
        for neighbor in dislikes[current]:
            if neighbor not in visited:
                visited[neighbor] = 1 if curr_color == 0 else 0
                queue.append(neighbor)
            else:
                if curr_color == visited[neighbor]:
                    return False
        
        #case for disconnected graph: you finished queue but still have not looked at all the nodes
        if len(queue) == 0 and len(visited) < len(dislikes):
            new_dislikes = {}
            for key, value in dislikes.items():
                if key not in visited:
                    new_dislikes[key] = value
            dislikes = new_dislikes
            queue = start_new_queue(dislikes, visited)
                
    return True

def start_new_queue(dislikes, visited):
    first_item = list(dislikes.keys())[0]
    visited[first_item] = 0
    return [first_item]
