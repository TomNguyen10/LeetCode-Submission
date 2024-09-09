# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, target, curr, dic):
            if not node:
                return 

            curr += node.val
            self.res += dic[curr-target]
            dic[curr] += 1

            dfs(node.left, target, curr, dic)
            dfs(node.right, target, curr, dic)

            dic[curr] -= 1
        self.res = 0
        dic = defaultdict(int)
        dic[0] += 1
        dfs(root, targetSum, 0, dic)
        return self.res
