# Partitioning a Graph

In this exercise you will take in an adjacency list and determine if you can divide dogs into two groups where no two dogs that are known for fighting each other are in the same group.  This is a variation on the [graph coloring](https://en.wikipedia.org/wiki/Graph_coloring) problem as it can be extended to breaking the graph into `k` groups, each labeled with a color.

## Learning Goals

In this exercise you should be able to:

- Work with an adjacency list to process a graph.
- Navigate a graph through a traversal

## Description

Given a set of N puppies, we would like to split them into two groups of any size to use two play areas.

Some dogs have a history of fighting with specific other dogs and shouldn't be put into the same play area.

Formally, if `dislikes[i] = [a, b]`, it means dog `i` is not allowed to put in the same group as dog `a` or dog `b`.

Dislike is mutual. If dog `a` that dislikes dog `b`, dog `b` also dislikes dog `a`. 

Return `True` if and only if it is possible to split the dogs into two groups where no fighting will occur. Otherwise, return `False`.

### Example 1
*Input*:
``` python
dislikes = { 
            "Fido": [],
            "Nala": ["Coper", "Spoto"],
            "Cooper": ["Nala", "Bruno"],
            "Spot": ["Nala"],
            "Bruno": ["Cooper"]
            }
```
*Output*: `True`
Explanation: group1: `["Fido", "Nala", "Bruno"]`, group2: `["Cooper", "Spot"]`

### Example 2
*Input*:
```python
dislikes = {
            "Fido": [],
            "Nala": ["Cooper", "Spot"],
            "Coooper": ["Nala", "Spot"],
            "Spot": ["Nala", "Cooper"]
            }
```
*Output*: `False`
Explanation: The nodes `Nala`, `Cooper`, and `Spot` are interconnected and so there is no way to split them up.

### Example 3
*Input*: 
```Python
dislikes = { 
            "Fido": [],
            "Nala": ["Cooper", "Cali"],
            "Cooper": ["Nala", "Spot"],
            "Spot": ["Cooper", "Bruno"],
            "Bruno": ["Spot", "Cali"],
            "Cali": ["Nala", "Bruno"]
            }
```
*Output*: `False`
Explanation: There is no way to split `Nala`, `Cooper`, `Spot`, `Bruno`, and `Cali` up into two groups such that they are all separated from the dogs they dislike.

## Source

- [Leetocde 886. Possible Bipartition](https://leetcode.com/problems/possible-bipartition/)
