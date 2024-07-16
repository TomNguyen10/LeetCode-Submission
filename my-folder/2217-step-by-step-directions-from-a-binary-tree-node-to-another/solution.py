# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(node, des, path):   
            if not node: return False

            if node.val == des: return True

            path.append('L')
            if dfs(node.left, des, path): return True
            path.pop()

            path.append('R')
            if dfs(node.right, des, path): return True
            path.pop()

            return False
        
        path1 = []
        path2 = []
        dfs(root, startValue, path1)
        dfs(root, destValue, path2)

        common = 0

        while common < len(path1) and common < len(path2) and path1[common] == path2[common]:
            common += 1
        
        res = []
        
        res.extend('U' * (len(path1) - common))

        res.extend(path2[common:])

        return "".join(res)

