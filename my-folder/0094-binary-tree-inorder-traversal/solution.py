# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def recur(root, arr):
            if not root:
                return 
            recur(root.left, arr)
            arr.append(root.val)
            recur(root.right, arr)
            return arr
        recur(root, res)
        return res
