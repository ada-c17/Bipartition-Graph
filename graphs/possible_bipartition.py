# Can be used for BFS


def possible_bipartition(dislikes):
    color = {}
    def dfs(current, curr_color):
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
        if node not in color:
            if not dfs(node, True):
                return False
    return True
            
        


