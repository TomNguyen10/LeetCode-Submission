# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum = 0
        def convert(node):
            if not node:
                return
            convert(node.right)
            node.val += self.sum
            self.sum = node.val
            convert(node.left)
        convert(root)
        return root
