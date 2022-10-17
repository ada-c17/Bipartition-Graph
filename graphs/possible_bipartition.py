# Can be used for BFS
from collections import defaultdict

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(E+V)
        Space Complexity: O(E+V)
    """
    
    def draw_colors(dog, color):
        color_table[dog] = color

        for other in dislikes[dog]:
            if color_table[other] == color:
                return False
        
            if color_table[other] == NOT_COLORED and (not draw_colors(other, -color)):
                return False
        
        return True
    
    
    NOT_COLORED, BLUE, GREEN = 0, 1, -1

    if len(dislikes) == 1 or not dislikes:
        return True
    
    color_table = defaultdict(int)

    for dog in dislikes:
        if color_table[dog] == NOT_COLORED and (not draw_colors(dog, BLUE)):
            return False

    return True