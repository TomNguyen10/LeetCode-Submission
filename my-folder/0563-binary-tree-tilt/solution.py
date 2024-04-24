# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val
            left = dfs(root.left)
            right = dfs(root.right)
            self.res += abs(left - right)
            return root.val + left + right
        val = dfs(root)
        return self.res
