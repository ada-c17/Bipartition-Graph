# Can be used for BFS
from collections import deque 

class Graph:
    def __init__(self, nodes : int):
        self.adjlist = []
        self.nodes = nodes

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    ## input: dislikes dictionary:
        ## dog names are key: [list of dogs that do not get along]
    ## output: True or False
        ## true if it is possible to split dogs into two groups
        ## false if it is not possible

    ## goal: create a graph with adjacency list
        ## navigate the graph through traversal
    
    #dictionary of nodes and its edges is a graph!

    #store dogs names, store relationship, and check if they can be
        # added to a group
    # nodes with connected edges cannot
        # be added to to group together

    pass

