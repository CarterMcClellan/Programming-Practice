"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        self.graph = defaultdict(list)
        return self.dfs(node)
    
    def dfs(self, node: 'Node'):
        val = node.val
        
        # if the node has already been seen
        # return it
        if val in self.graph:
            return self.graph[val]
        
        # otherwise create our copy
        copy = Node(val)
        self.graph[val] = copy
        
        # initialize all neighbors of a
        # given copy (and their neighbors if need be)
        for neighbor in node.neighbors:
            copy_of_neighbor = self.dfs(neighbor)
            copy.neighbors.append(copy_of_neighbor)
        
        # return a copy
        return copy
