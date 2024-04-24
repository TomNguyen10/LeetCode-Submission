# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.min1 = self.min2 = float('inf')
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            if node.val < self.min1:
                self.min2 = self.min1
                self.min1 = node.val
            elif node.val < self.min2 and node.val != self.min1:
                self.min2 = node.val
            inOrder(node.right)
        inOrder(root)
        if self.min1 == self.min2 or self.min2 == float('inf'):
            return -1
        return self.min2

