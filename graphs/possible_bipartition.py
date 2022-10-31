# Can be used for BFS
from collections import deque
from ssl import VERIFY_X509_STRICT 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    if not dislikes:
        return True

    first_dog = list(dislikes.keys())[0]

    groups = {}




