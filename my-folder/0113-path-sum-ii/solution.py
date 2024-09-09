# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        def dfs(root, target, curr):
            if not root:
                return 
            if not root.left and not root.right and target == root.val:
                self.res.append(curr + [root.val])
                return
            dfs(root.left, target - root.val, curr + [root.val])
            dfs(root.right, target - root.val, curr + [root.val])
        dfs(root, targetSum, [])
        return self.res
