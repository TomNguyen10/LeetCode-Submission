# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
        def dfs(node, level, depth, val):
            if not node:
                return
            if level + 1 == depth:
                left = node.left
                right = node.right
                node.left = TreeNode(val)
                node.right = TreeNode(val)
                node.left.left = left
                node.right.right = right
            dfs(node.left, level + 1, depth, val)
            dfs(node.right, level + 1, depth, val)
        dfs(root, 1, depth, val)
        return root
