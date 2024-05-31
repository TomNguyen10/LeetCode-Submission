# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def getHeight(node):
            if not node:
                return 0
            return 1 + max(getHeight(node.left), getHeight(node.right))
        
        height = getHeight(root)
        width = 2**height - 1
        self.res = [["" for _ in range(width)] for _ in range(height)]

        def update(node, row, left, right):
            if not node:
                return
            mid = (left + right) // 2
            self.res[row][mid] = f"{node.val}"
            update(node.left, row + 1, left, mid - 1)
            update(node.right, row + 1, mid + 1, right)
        
        update(root, 0, 0, width - 1)
        return self.res
