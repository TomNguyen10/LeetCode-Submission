# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.res = []

        def preOrder(node):
            if not node:
                return
            self.res.append(node)
            preOrder(node.left)
            preOrder(node.right)
        
        preOrder(root)

        for i in range(len(self.res) - 1):
            self.res[i].left = None
            self.res[i].right = self.res[i+1]
