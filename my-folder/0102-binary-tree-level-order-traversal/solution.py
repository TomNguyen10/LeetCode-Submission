# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        def bfs(root, arr):
            queue = [root]

            while queue:
                temp = []

                size = len(queue)
                
                for i in range(size):
                    node = queue.pop(0)
                    temp.append(node.val)
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)

                arr.append(temp)

        res = []

        bfs(root, res)

        return res
