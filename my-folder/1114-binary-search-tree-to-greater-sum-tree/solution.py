# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.list = []
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            self.list.append(node)
            inOrder(node.right)
        
        inOrder(root)
        val = 0
        for i in range(len(self.list) - 1, -1, -1):
            node = self.list[i]
            curr = node.val
            node.val += val
            val += curr

        return root
