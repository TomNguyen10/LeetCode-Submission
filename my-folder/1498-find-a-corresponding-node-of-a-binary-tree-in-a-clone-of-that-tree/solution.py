# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original and not cloned:
            return
        if original.val == target.val:
            return cloned
        left = self.getTargetCopy(original.left, cloned.left, target)
        right = self.getTargetCopy(original.right, cloned.right, target)
        if left:
            return left
        return right
