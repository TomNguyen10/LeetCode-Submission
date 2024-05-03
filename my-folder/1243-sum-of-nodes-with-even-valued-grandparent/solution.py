# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(grandparent, parent, current):
            if not current:
                return
            if grandparent and grandparent.val % 2 == 0:
                self.res += current.val
            dfs(parent, current, current.left)
            dfs(parent, current, current.right)
        dfs(None, None, root)
        return self.res
