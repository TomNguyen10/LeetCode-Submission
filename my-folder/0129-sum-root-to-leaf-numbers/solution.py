# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        numbers = []

        def dfs(root, curr, arr):
            curr = curr * 10 + root.val

            if root.left:
                dfs(root.left, curr, arr)
            if root.right:
                dfs(root.right, curr, arr)
            
            elif not root.left and not root.right:
                arr.append(curr)
            
        dfs(root, 0, numbers)

        print(numbers)

        return sum(numbers)
