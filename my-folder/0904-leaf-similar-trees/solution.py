# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def sequence(root, arrList):
            if not root.left and not root.right:
                arrList.append(root.val)
            if root.left:
                sequence(root.left, arrList)
            if root.right:
                sequence(root.right, arrList)
            return arrList
        
        arr1 = sequence(root1, [])
        arr2 = sequence(root2, [])

        return arr1 == arr2

