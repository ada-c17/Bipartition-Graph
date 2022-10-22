from __future__ import annotations
# Can be used for BFS
from collections import deque 
from typing import Dict, List, Optional, Set

def possible_bipartition(dislikes: Dict[str, List[str]]) -> bool:
    groups = {"a":set(), "b":set()}
    queue = deque(dislikes.keys())

    while queue:
        n = len(queue)
        for _ in range(n):
            pup = queue.popleft()
            if classify_pups(pup, set(dislikes[pup]),queue, groups) is False:
                return False
        if queue and len(queue) == n:
            pup = queue.popleft()
            groups["a"].add(pup)
            groups["b"] = groups["b"].union(set(dislikes[pup]))
    return True

def classify_pups(pup: str, disliked_pups: Set, queue: deque, groups: Dict) -> Optional[bool]:
    if disliked_pups.intersection(groups["a"]):
        if disliked_pups.intersection(groups["b"]):
                return False
        else:
            groups["b"].add(pup)
            groups["a"] = groups["a"].union(disliked_pups)
    if pup not in groups["a"].union(groups["b"]):
        if disliked_pups.intersection(groups["b"]):
            groups["a"].add(pup)
            groups["b"] = groups["b"].union(disliked_pups)
        else:
            # not ready to classify pup
            queue.append(pup)
