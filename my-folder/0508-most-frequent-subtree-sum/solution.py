# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.dic = defaultdict(int)
        def dfs(node):
            if not node:
                return 0
            value = node.val
            value += dfs(node.left)
            value += dfs(node.right)
            self.dic[value] += 1
            return value
        dfs(root)
        max_val = max(self.dic.values())
        res = [key for key, val in self.dic.items() if val == max_val]
        return res
