# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.node1 = self.node2 = self.prev = None

        def inOrder(root):
            if not root:
                return

            inOrder(root.left)

            if self.prev and self.prev.val > root.val:
                if not self.node1:
                    self.node1 = self.prev
                self.node2 = root
            self.prev = root

            inOrder(root.right)

        inOrder(root)

        if self.node1 and self.node2:
            self.node1.val, self.node2.val = self.node2.val, self.node1.val
