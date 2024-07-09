# Definition for a binary tree node.
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inOrder(root):
            if not root:
                return []
            return inOrder(root.left) + [root.val] + inOrder(root.right)
        
        list1 = inOrder(root1)
        list2 = inOrder(root2)
        
        res = []
        i = j = 0
        
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                res.append(list1[i])
                i += 1
            else:
                res.append(list2[j])
                j += 1
                
        res.extend(list1[i:])
        res.extend(list2[j:])
        
        return res

