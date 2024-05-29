# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.dic = defaultdict(int)
        def dfs(node):
            if not node:
                return
            self.dic[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        max_val = max(self.dic.values())
        res = [key for key, val in self.dic.items() if val == max_val]
        return res
