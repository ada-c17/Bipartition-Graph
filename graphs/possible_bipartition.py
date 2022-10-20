from __future__ import annotations
# Can be used for BFS
from collections import deque 
from typing import Dict, List, Optional

def possible_bipartition(dislikes: Dict[str, List[str]]) -> bool:
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    groups = {"a":set(), "b":set()}
    store = deque(dislikes.keys())

    while store:
        n = len(store)
        for _ in range(n):
            pup = store.popleft()
            result = classify_pups(pup, set(dislikes[pup]), groups)
            if result is False:
                return False
            elif result:
                store.append(pup)
        if store and len(store) == n:
            pup = store.popleft()
            groups["a"].add(pup)
            for d_pup in dislikes[pup]:
                groups["b"].add(d_pup)
    return True

def classify_pups(pup: str, disliked_pups: set, groups: object) -> Optional[str | bool]:
    if disliked_pups.intersection(groups["a"]):
        if disliked_pups.intersection(groups["b"]):
                return False
        else:
            groups["b"].add(pup)
            for d_pup in disliked_pups:
                groups["a"].add(d_pup)
    if pup not in groups["a"].union(groups["b"]):
        if disliked_pups.intersection(groups["b"]):
            groups["a"].add(pup)
            for d_pup in disliked_pups:
                groups["b"].add(d_pup)
        else:
            # not ready to classify pup
            return pup
    return None
