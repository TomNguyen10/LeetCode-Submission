# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        def dfs(node, target, current):
            if not node:
                return
            if not node.left and not node.right and target == node.val:
                self.res.append(current + [node.val])
                return
            dfs(node.left, target - node.val, current + [node.val])
            dfs(node.right, target - node.val, current + [node.val])
        dfs(root, targetSum, [])
        return self.res
