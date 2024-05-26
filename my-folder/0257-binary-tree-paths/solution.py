# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res = []

        def dfs(node, current):
            if not node:
                return
            if current:
                current += f"->{node.val}"
            else:
                current += f"{node.val}"
            if not node.left and not node.right:
                self.res.append(current)
            dfs(node.left, current)
            dfs(node.right, current)
        
        dfs(root, "")

        return self.res
