# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []

        def bfs(root, arr):
            queue = [root]

            while queue:
                size = len(queue)
                total = 0
                for i in range(size):
                    node = queue.pop(0)
                    total += node.val
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
            
                value = total / size
                arr.append(value)
        
        res = []
        bfs(root, res)
        return res
