# Can be used for BFS
from collections import deque
from locale import currency


def possible_bipartition(dislikes):
    color = {}
    def dfs(current, curr_color):
        neighbors = dislikes[current]
        if current in color:
            if color[current] != curr_color:
                return False
            else:
                return True
        else:
            color[current] = curr_color
        for each_node in dislikes[current]:
            if not dfs(each_node, not curr_color):
                return False
        return True
    
    for node in dislikes.keys():
        neighbors = dislikes[node]
        if node not in color:
            if not dfs(node, True):
                return False
    return True
            
        


