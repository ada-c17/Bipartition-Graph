# Can be used for BFS
from collections import deque 

# source used for help with solution: https://www.geeksforgeeks.org/check-if-a-given-graph-is-bipartite-using-dfs/

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    
    if not dislikes:
        return True

    visited = {}
    color = {}

    #run a DFS starting at each key, to check if that graph is bipartite
    for each_key in dislikes:

        #make starting dicts
        for item in dislikes:
            visited[item] = False
            color[item] = False

        first_key = each_key
        visited[first_key] = True
        color[first_key] = False
        if not isBipartite(dislikes, first_key, visited, color):
            return False
    
    # if we get through all keys without finding a non-bipartite cycle, return true
    return True

def isBipartite(dislikes, item, visited, color):

    for name in dislikes[item]:
        # if the name hasn't been visited, recurse on its dislikes
        if visited[name] == False:
            visited[name] = True
            color[name] = not color[item]
            if not isBipartite(dislikes, name, visited, color):
                return False
        # if the name already has been visisted and had to be set to the same color, its not bipartite      
        elif color[name] == color[item]:
            return False
    return True





    # def dfs_helper(current, visited, graph):
    #     if current not in visited:
    #         visited.append(current)
    #         for neighbor in graph[current]:
    #             self.dfs_helper(neighbor, visited, graph)

    # def dfs(self):
    #     graph = self.adjacency_dict
    #     if len(graph) == 0:
    #         return []
    #     first_item = list(graph.keys())[0]
    #     visited = []
    #     self.dfs_helper(first_item, visited, graph)
    #     return visited