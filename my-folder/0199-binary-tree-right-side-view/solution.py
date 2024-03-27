# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root: return []

        def bfs(root, arr):
            queue = [root]

            while queue:
                size = len(queue)
                for i in range(size):
                    curr = queue.pop(0)
                    if i == 0:
                        arr.append(curr.val)
                    if curr.right: 
                        queue.append(curr.right)
                    if curr.left:
                        queue.append(curr.left)
            
        res = []
        bfs(root, res)
        return res
