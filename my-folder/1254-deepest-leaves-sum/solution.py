# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def getHeight(node):
            if not node:
                return 0
            return 1 + max(getHeight(node.left), getHeight(node.right))
        self.depth = getHeight(root)
        self.res = 0
        def dfs(node, cur_depth):
            if not node:
                return
            if cur_depth == self.depth:
                self.res += node.val
            else:
                dfs(node.left, cur_depth + 1)
                dfs(node.right, cur_depth + 1)
        
        dfs(root, 1)
        return self.res
                
