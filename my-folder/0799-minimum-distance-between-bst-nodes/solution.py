# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.res = float('inf')
        self.pre = None  
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            if self.pre is not None: 
                self.res = min(self.res, node.val - self.pre)  
            self.pre = node.val  
            inOrder(node.right)
        inOrder(root)
        return self.res

