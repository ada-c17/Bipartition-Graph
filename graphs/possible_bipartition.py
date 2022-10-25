def possible_bipartition(dislikes):            

    def dfs(v, color):
        if v in groups:
            if color != groups[v]:
                return False
        else:
            groups[v] = color
            for nei in dislikes[v]:
                if not dfs(nei, color ^ 1): #change group/color interchangebly
                    return False
        return True
			
    groups = {}
    #tracks visited or not and which group it belongs to 
    for v in dislikes:
        if v not in groups:
            if not dfs(v, 0):
                return False
    return True