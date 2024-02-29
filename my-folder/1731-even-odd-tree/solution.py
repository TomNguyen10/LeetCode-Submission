# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = []
        queue.append(root)
        even = True

        while queue:
            size = len(queue)
            prevVal = float('-inf') if even else float('inf')

            for _ in range(size):
                node = queue.pop(0)
                if even and (node.val % 2 == 0 or node.val <= prevVal):
                    return False
                if not even and (node.val % 2 == 1 or node.val >= prevVal):
                    return False
                prevVal = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            even = not even
            
        return True

