# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(root, st):
            if not root:
                return 0
            if root.val in st:
                st.remove(root.val)
            else:
                st.add(root.val)
            if not root.left and not root.right:
                if len(st) <= 1:
                    return 1
                else:
                    return 0
            return dfs(root.left, st.copy()) + dfs(root.right, st.copy())


        return dfs(root, set())
