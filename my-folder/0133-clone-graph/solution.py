"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        self.dic = {}
        def dfs(node, visited):
            if node in visited:
                return
            self.dic[node] = Node(node.val)
            visited.add(node)
            for neighbor in node.neighbors:
                dfs(neighbor, visited)
        visited = set()
        dfs(node, visited)
        for key, val in self.dic.items():
            neigh = []
            for neighbor in key.neighbors:
                neigh.append(self.dic[neighbor])
            val.neighbors = neigh
        return self.dic[node]
        

