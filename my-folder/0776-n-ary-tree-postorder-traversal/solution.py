"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.res = []
        def bfs(node):
            if not node: return

            children = node.children

            for child in children:
                bfs(child)

            self.res.append(node.val)

        if not root: return self.res

        bfs(root)

        return self.res
            

