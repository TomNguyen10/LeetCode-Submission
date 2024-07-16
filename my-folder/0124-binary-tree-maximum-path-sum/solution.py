# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def get_max(node):
            if not node: return 0

            left = max(get_max(node.left), 0)
            right = max(get_max(node.right), 0)

            current = node.val + left + right
            self.res = max(self.res, current)

            return node.val + max(left, right)
        get_max(root)
        return self.res
