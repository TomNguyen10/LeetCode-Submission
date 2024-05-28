# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root, arrList, ans, total, target):
            if not root:
                return 
            total += root.val
            arrList.append(root.val)
            if total == target and not root.left and not root.right:
                ans.append(arrList[:])
            dfs(root.left, arrList, ans, total, target) 
            dfs(root.right, arrList, ans, total, target)
            arrList.pop()

        total = 0
        arrList, ans = [], []
        dfs(root, arrList, ans, total, targetSum)
        return ans
