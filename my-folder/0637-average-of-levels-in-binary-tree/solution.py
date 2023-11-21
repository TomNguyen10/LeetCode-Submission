# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        queue = []
        if not root:
            return res
        queue.append(root)
        while queue:
            n = len(queue)
            total = 0
            for i in range(n):
                node = queue.pop(0)
                print(node.val)
                total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            add = total/n
            res.append(add)
        return res

