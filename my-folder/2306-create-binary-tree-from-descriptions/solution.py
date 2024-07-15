# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hash_map = {}
        children = set()
        for parent, child, isLeft in descriptions:
            if parent not in hash_map:
                hash_map[parent] = TreeNode(parent)
            if child not in hash_map:
                hash_map[child] = TreeNode(child)
            if isLeft == 1:
                hash_map[parent].left = hash_map[child]
            else:
                hash_map[parent].right = hash_map[child]
            children.add(child)
        root = None
        for parent, child, isLeft in descriptions:
            if parent not in children:
                root = hash_map[parent]
                break
        return root

