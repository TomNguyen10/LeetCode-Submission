# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        def dfs(node, target):
            ans = 0
            if not node:
                return ans
            if node.val == target:
                ans += 1
            ans += dfs(node.left, target - node.val)
            ans += dfs(node.right, target - node.val)
            return ans
        return dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
