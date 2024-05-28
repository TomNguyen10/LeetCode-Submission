# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        max_sum = float('-inf')
        res = 1
        level = 1
        while q:
            current_sum = 0
            size = len(q)
            for i in range(size):
                node = q.popleft()
                current_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if current_sum > max_sum:
                max_sum = current_sum
                res = level
            level += 1
        return res



