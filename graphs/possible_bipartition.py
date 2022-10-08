from __future__ import annotations
# Can be used for BFS
from collections import deque 
from typing import Dict, List, Optional, Tuple

def possible_bipartition(dislikes: Dict[str, List[str]]) -> bool:
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    groups = {"a":[], "b":[]}
    store = deque()
    for pup, disliked_pups in dislikes.items():
        store.append(classify_pups(pup, disliked_pups, groups))

    while store:
        result = process_store(store, groups)
        if result is False:
            return False
        store = result
    return True

def classify_pups(pup, disliked_pups, groups) -> Optional[Tuple[str, List[str]]] | bool:
    if any([d_pup in groups["a"] for d_pup in disliked_pups]):
        if any([d_pup in groups["b"] for d_pup in disliked_pups]):
                return False
        else:
            if pup not in groups["b"]:
                groups["b"].append(pup)
            for d_pup in disliked_pups:
                if d_pup not in groups["a"]:
                    groups["a"].append(d_pup)
    if pup not in groups["a"] and pup not in groups["b"]:
        if any([d_pup in groups["b"] for d_pup in disliked_pups]):
            groups["a"].append(pup)
            for d_pup in disliked_pups:
                if d_pup not in groups["b"]:
                    groups["b"].append(d_pup)
        else:
            return pup, disliked_pups
    return None

def process_store(store, groups) -> deque | bool:
    n = len(store)
    for _ in range(n):
        pup, disliked_pups = store.popleft()
        result = classify_pups(pup, disliked_pups, groups)
        if result is False:
            return False
        elif result:
            store.append(result)
    if store and len(store) == n:
        pup, disliked_pups = store.popleft()
        groups["a"].append(pup)
        for d_pup in disliked_pups:
            if d_pup not in groups["b"]:
                groups["b"].append(d_pup)
    return store
