# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, min_val, max_val):
            if not root:
                return True
            if root.val <= min_val:
                return False
            if root.val >= max_val:
                return False
            return dfs(root.left, min_val, root.val) and dfs(root.right, root.val, max_val)
        
        return dfs(root, float('-inf'), float('inf'))
